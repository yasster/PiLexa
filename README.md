# PiLexa


This contains the code for an unpublished skill that allows users to block social media on the local network. For example, a user might say:

"Alexa, Tell RaspberryPI StudyMode turn on"

or

"Alexa, Tell RaspberryPI StudyMode turn off"


## Setup Process

1. Go on https://developer.amazon.com/ and log in with a developer account. Navigate to the "Alexa" tab and click on "Alexa Skills Kit."
2. Click on "Add Skill." You will be taken to a setup menu.
3. __Skill Information__ page: give the skill a name you choose. For Invocation Name, put 'raspberrypi' and in the Global Fields section, mark that the skill uses audio player directives.
4. __Interaction Model__ page: put the following under Intent Schema.
```
{
  "intents": [
    {
      "slots": [
        {
          "name": "status",
          "type": "mode"
        }
      ],
      "intent": "StudyMode"
    }
  ]
}

```
Next, in the Sample Utterances section, put this.
```
StudyMode turn {status}

```
5. Add a custom slot type called mode. Under "Values", put:
```
on | off

```
6. __Configuration__ page: under Endpoint, select __HTTPS__ as the Service Endpoint Type. Select North America/Europe depending on where you are. In the field that pops up, leave that blank for now. We will come back to that once the skill has been uploaded to Lambda. Also, under Account Linking, make sure that 'no' is checked.

7. on Default put your ngrogk address, we used 
```
https://pilocal.ngrok.io

```

8. Go to the __Test__ page and set Enabled to true. The skill will now work exclusively on your devices.

## Technical Details

I.Make sure to have a subdomain of Ngrok enabled on the raspberry pi
```
./ngrok https 5000 -subdomain pilocal
```
II. Execute the ngrok command! The pi-control.py should have exectued from the startup.sh




