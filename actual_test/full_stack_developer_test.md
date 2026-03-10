# Full Stack Developer - Technical test

In this test you will create, validate, and document a working REST API using FastAPI, based on a simple model. 

This test is to assess familiarity with core web technologies (including REST API), Python, the FastAPI framework, troubleshooting (handling errors), standards specification documents, and online documentation & guidance.

## Create, validate, and document a working REST API using FastAPI

This test is to assess familiarity with core web technologies (including REST API), Python, the FastAPI framework, and with troubleshooting (handling errors), and accessing documentation and guidance.

### Create a FastAPI instance

Create a FastAPI implementation of the below **Client** model. 

```yaml
client_key: 3fa85f64-5717-4562-b3fc-2c963f66afa6
slk: LISRE010819941
forename: Frederico
preferred_forename: Fred
family_name: Flintstone
pronoun: He/him
date_of_birth: 2001-03-06
gender: 1
intersex: 0
sexual_orientation: 1
indigenous_status: 4
country_of_birth: 1101
main_lang_at_home: 1201
phone: 0412999999
email: fred@flinstone.com.au
suburb: string
state: VIC
postcode: MALVERN EAST
consent_mail: true
consent_email: true
consent_voice_message: true
consent_sms: true
```

The use of Co-pilot or other code generators is not permitted. 

The API should have at least a GET and POST endpoint (i.e. a full implementation is not required). You may prefer to add other functionality. 

#### Include validation on a POST

Implement validation of a request to the instantiated API. 

A test must be implemented of the validation, so that it passes a valid request, and fails an invalid request. 

### Test implementation

Implement a set of tests for the above API to validate it meets basic requirements. 

Tests should be automated using a framework such as [pytest](https://docs.pytest.org/en/stable/).

A combination of functional and unit tests of both positive and negative types are expected.

The approach for testing is your decision. 

You may use the test below data. There are a few errors in the data, which are placed there deliberately. 

### Document the API

Formally document the API in a Markdown formatted file. As it is a simple resource, we would not expect lengthy documentation but it should be professionally structured. 

### Other information

For reviewing you are encouraged to keep rough notes of your implementation, especially to describe challenges, caveats, known flaws. 

## Test data

```csv
id,client_key,slk,forename,preferred_forename,family_name,pronoun,date_of_birth,gender,intersex,sexual_orientation,indigenous_status,country_of_birth,main_lang_at_home,phone,email,suburb,state,postcode,consent_email,consent_sms
3365,b9d48636-095b-4170-8c66-36bf06568fb0,OUECT050319643,Actions,,Mouse,,1964-03-05,TM,,,4,1101,1201,412121121,,,,9999,1,1
3361,76b235df-6315-4698-8b87-e6f5aca82734,EIHEI010120019,Keith,,Keith,,2001-01-01,M,,,,,,411111111,sarah@test.com,ABBEY,WA,6280,0,0
3360,50f89b4a-9733-4501-aa15-28b517bd88fe,GUEUC031119951,Lucas,,Nguyen,he/him,1995-11-03,M,,,9,2102,1201,498765432,,BALLINA,NSW,2478,0,1
3359,2cc2787e-e843-42c3-8c77-75e095522886,AREMI140619882,Emily,,Harper,,1988-06-14,F,2,ST,1,1101,1201,412345678,,LISMORE HEIGHTS,NSW,2480,0,0
3358,3c5d4b4f-cfb7-4d01-a1f4-bd701e0a0508,OBIAR200719902,Margot,,Robbie,she/her,1990-07-20,F,2,ST,4,1101,1201,412345678,,TOORMINA,NSW,2452,0,0
3357,10061e60-d072-4d58-8db5-1a6fa09030d7,MIHTE080819901,Steven,,Smith,he/him,1990-08-08,M,2,GA,4,1101,1201,93000000,,COFFS HARBOUR,NSW,2450,0,1
3354,9d777224-d828-4fa5-a717-79469b58295a,NGGOL011019999,Polly,,Engage,,1999-10-01,,,,4,9999,,400000000,,Blacktown,NSW,2148,0,0
3350,8c6f8860-0c92-458d-ad69-83371ac5526e,INOSA050319972,Isabella,,Linton,She/Her,1997-03-05,F,,,,,,498765432,,AARONS PASS,NSW,2850,0,0
3349,bc15c1a5-6c4a-46ee-90dd-62b44b02d9b2,ARSAT090219982,Catherine,,Earnshawe,She/Her,1998-02-09,F,,,4,2102,1201,401234567,,LIVERPOOL WESTFIELD,NSW,2170,0,0
3348,3b3e3171-0f96-412f-8019-d0664f814280,NKOOP090999993,Sophie,,Unknown,,9999-09-09,UN,9,ST,1,,,40000000,,HOBART,TAS,7000,1,1
3347,98b41f87-d348-47a1-931a-d9da3bc81bf4,ORMAT141019782,Katherine,,FOREMAN,She/Her,1978-10-14,F,,UN,9,9999,2901,412345678katherine@forman.com.au,,Nuriootpa,SA,5355,0,0
3346,acb7ee97-7a36-4c9c-83a8-7c2b50741055,EWTTE130219942,Stephanie,,Hewitt,She/Her,1994-02-13,F,,UN,9,9999,1201,402112511,,Adelaide,SA,5000,0,0
```



# Client Model Specification

| Field Name         | Description                                                  | Constraints | Data type    |
| ------------------ | ------------------------------------------------------------ | ----------- | ------------ |
| client_key         | GUID to uniquely identify client                             |             | uuid         |
| slk                | Aligns with [PMHC-MDS client.slk](https://docs.pmhc-mds.com/projects/data-specification/en/v5.0/data-model-and-specifications.html#statistical-linkage-key) |             |              |
| forename           |                                                              | Not null    | string(256)  |
| preferred_name     |                                                              | Nullable    | string(256)  |
| family_name        |                                                              | Not null    | string(256)  |
| pronoun            | This field captures the client's preferred pronouns. Valid options include: <br/>0: He/Him<br/>1: She/Her<br/>2: They/Them<br/>3: She/Them<br/>4: He/Them<br/>5: Name only<br/>6: Prefer to self-describe<br/>7: Prefer not to say | Nullable    | string       |
| date_of_birth      | Options are the same as PMHC-MDS [Date of Birth](https://docs.pmhc-mds.com/projects/data-specification/en/v4/data-model-and-specifications.html#date-of-birth) | Not null    | date         |
| gender             | Options are the same as [FHIR PCORNet Gender Identity Codes](https://build.fhir.org/ig/HL7/cdmh/CodeSystem-pcornet-gender-identity.html) | Nullable    | string       |
| intersex           | Valid options: <br />1=Yes<br />2=No<br />3=Does not wish to disclose<br />9=Not stated/unknown |             |              |
| sexual_orientation | Options are the same as [FHIR ValueSet Sexual Orientation](https://build.fhir.org/ig/HL7/cdmh/ValueSet-pcornet-sexual-orientation.html) | Nullable    | string       |
| indigenous_status  | Options are the same as PMHC-MDS [Aboriginal and Torres Strait Islander Status](https://docs.pmhc-mds.com/projects/data-specification/en/v4/data-model-and-specifications.html#aboriginal-and-torres-strait-islander-status) | Nullable    | string       |
| country_of_birth   | Options are the same as PMHC-MDS [Country of Birth](https://docs.pmhc-mds.com/projects/data-specification/en/v4/data-model-and-specifications.html#country-of-birth) | Nullable    | string (256) |
| main_lang_at_home  | Options are the same as PMHC-MDS [Main Language Spoken at Home](https://docs.pmhc-mds.com/projects/data-specification/en/v4/data-model-and-specifications.html#main-language-spoken-at-home) | Nullable    | string(256)  |
| phone              |                                                              | Not null    | string(20)   |
| email              |                                                              | Nullable    | string(256)  |
| suburb             |                                                              | Nullable    | string(256)  |
| state              |                                                              |             |              |
| postcode           |                                                              |             |              |
| consent_email      |                                                              | n/a         | boolean      |
| consent_sms        |                                                              | n/a         | boolean      |

