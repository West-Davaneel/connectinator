# Connectinator

West Davaneel's latest innovation!


## Installation


Install and run locally.

**👩‍👧 Clone repository**


<div class="termy">

```console
$ git clone https://github.com/West-Davaneel/connectinator.git
---> 100%
```

</div>

** Navigate into the repository ** 

<div class="termy">

```console
$ cd connectinator
// Now you are in the repostiory 😁
```

</div>


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



**Run app**

<div class="termy">

```console
$ python .\app.py

DEBUG:slack_bolt.App:Sending a request 
INFO:slack_bolt.App:A new session has been established (session id: 123456)
INFO:slack_bolt.App:Bolt app is running!
```

</div>