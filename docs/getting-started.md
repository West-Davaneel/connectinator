# Getting Started

Connecticator is built using [Bolt](https://slack.dev/bolt-python/tutorial/getting-started), Slack's official Python framework for creating apps. You might wanna check out their [docs](https://slack.dev/bolt-python/tutorial/getting-started), or view [Resources](/resources), before continuing. 

## Installation

Install and run Connecticator locally. 

!!! note
    If you are not a part of West Davaneel, you will have to [create a Slack App](https://slack.dev/bolt-python/tutorial/getting-started).

### Clone Repository


<div class="termy">

```console
$ git clone https://github.com/West-Davaneel/connectinator.git
---> 100%
```

</div>

**🔍 Navigate into the repository ** 

<div class="termy">

```console
$ cd connectinator
// Now you are in the repostiory 😁
```

</div>

Looking into the repository folder, you should be seeing something like this:

```
└───connecticator           <-- The repository folder
    ├───connecticator       <-- Helper modules, classes, functions
	├───docs                <-- Documentation
	├───.env.example        <-- Example .env file
	├───requirements.txt    <-- Requirements (dependencies)
	└───app.py              <-- Runs the Connecticator App
```

### Set up environment

**🤫 Get environmental variables**

These are variables that should not be hardcoded in, either for customization or security. 

!!! warning
    We keep the API keys in environmental variables -- NEVER commit them!

```hl_lines="7"
└───connecticator           
    ├───connecticator       
	├───docs               
	├───.env.example        
	├───requirements.txt    
	├───app.py             
    └───.env                <-- Create this file!
```
You must create a file named `.env` and supply these variables. These variables are either given to you or you must obtain them following the [Bolt Python](https://slack.dev/bolt-python/tutorial/getting-started) tutorial.

??? example
     You can see the `.env.example` as an example:  

    ```
    --8<-- ".env.example"
    ```

**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

=== "macOS/Linux"

    ```
    python3 -m venv env
    ```

=== "Windows Command Line"

    ```
    python -m venv env
    ```

=== "Windows Powershell"

    ```
    python -m venv env
    ```

The last argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

=== "macOS/Linux"

    ```
    source env/bin/activate
    ```

=== "Windows Command Line"

    ```
    .\env\Scripts\activate.bat
    ```

=== "Windows Powershell"

    ```
    .\env\Scripts\activate.ps1
    ```


**📦 Install packages**

<div class="termy">

```console
$ python -m pip install -r requirements.txt

---> 100%
```

</div>


### Run the app

The app does not Hot Reload when changes are made -- you will have to restart the app for any changes to come into effect.

<div class="termy">

```console
$ python .\app.py

DEBUG:slack_bolt.App:Sending a request 
INFO:slack_bolt.App:A new session has been established (session id: 123456)
INFO:slack_bolt.App:Bolt app is running!
```

</div>