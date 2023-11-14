*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  merja  kissa1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  kk  kalle123
    Output Should Contain  Username must contain at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  merjaMerjanen  kissa1234
    Output Should Contain  Username must contain only lowercase letters (a-z)

Register With Valid Username And Too Short Password
    Input Credentials  merja  kis54
    Output Should Contain  Password must contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  merjamerjanen  kissakissa
    Output Should Contain  Password must contain letters and numbers or special characters

*** Keywords ***
Create User And Input New Command 
    Create User  kalle  kalle123    # <-- creates a user so that a test can
    Input New Command                               # check if the username already exists
