
import pandas as pd
import openai

# Configure OpenAI API (replace YOUR_API_KEY with your actual key)
openai.api_key = "YOUR_API_KEY"


def extract_validation_rules(instructions):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant for regulatory data profiling."},
            {"role": "user", "content": instructions}
        ]
    )
    rules = response['choices'][0]['message']['content']
    return rules

DataProfilingRules = [
        "Account Balance must be non-negative.",
        "Reported Amount must match Transaction Amount.",
        "Transaction Date should not be in the future." ,
        "Currency should be a valid ISO 4217 currency code",
        "High Rish Transactions should be flagged",
        "Round number Transactions should be checked for Money laundering"
    ]

def validate_data(SD ,CD,DataProfilingRules):
    SD['Currency'] = SD['Currency'].str.strip()
    CD['AlphabeticCode'] = CD['AlphabeticCode'].str.strip()
    Sampledata = pd.merge(SD,CD,left_on="Currency",right_on="AlphabeticCode")
    SampleData = pd.DataFrame(Sampledata, columns = ['Customer ID', 'Account Balance', 'Transaction Amount','Reported Amount','Currency','Country','Transaction Date','Risk Score'])
    FormatSampleDate = SampleData.drop_duplicates().copy()
    print(FormatSampleDate)
    errors = []
    for index, row in FormatSampleDate.iterrows():
       
        if row['Account Balance'] < 0:
            errors.append(f"Row {index}: "+ DataProfilingRules[0])
        if row['Transaction Amount'] != row['Reported Amount']:
            errors.append(f"Row {index}: "+ DataProfilingRules[1])
        if pd.to_datetime(row['Transaction Date']) > pd.Timestamp.now():
            errors.append(f"Row {index}: "+ DataProfilingRules[2])
        if row['Currency']=="Nan":
            errors.append(f"Row {index}: "+DataProfilingRules[3])
        if row['Transaction Amount'] > 5000:
            errors.append(f"Row {index}: "+DataProfilingRules[4])
        if row['Transaction Amount'] == round(row['Transaction Amount']):
            errors.append(f"Row {index}: "+DataProfilingRules[5])
       
    return errors

def suggest_remediation_actions(errors):
    remediations = []
    for error in errors:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant providing remediation actions for flagged errors."},
                {"role": "user", "content": f"Error: {error}. Suggest a remediation action."}
            ]
        )
        remediation = response['choices'][0]['message']['content']
        remediations.append(remediation)
    return remediations

samplefilepath = "SampleData.csv"
SampleData = pd.read_csv(samplefilepath)
print (SampleData)
currencyfilepath ="ISOCurrencyCodes.csv"
CurrencyData =  pd.read_csv(currencyfilepath)
print(CurrencyData)

DataProfilingRules = [
        "Account Balance must be non-negative.",
        "Reported Amount must match Transaction Amount.",
        "Transaction Date should not be in the future." ,
        "Currency should be a valid ISO 4217 currency code",
        "High Rish Transactions should be flagged",
        "Round number Transactions should be checked for Money laundering"
    ]
print (DataProfilingRules[1])

# Execution
# Extracting validation rules
instructions = "Extract and refine validation rules for the given dataset."
DataProfilingRules = extract_validation_rules(instructions)


print("\nValidating data...")
validation_errors = validate_data(SampleData,CurrencyData,DataProfilingRules)
print(validation_errors)

# Suggesting remediation actions

remediation_actions = suggest_remediation_actions(validation_errors)
print(remediation_actions)
