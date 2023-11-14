*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kallekallunen  kalleKallunen123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kallekallunen  kalleKallunen456
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  gugugaga  kalleKallunen123
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kallekallunen  kalleKallunen123
    Input Login Command
