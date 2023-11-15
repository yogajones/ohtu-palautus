*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  merja
    Set Password  merja123
    Set Password Confirmation  merja123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  m
    Set Password  merja123
    Set Password Confirmation  merja123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long    

Register With Valid Username And Invalid Password
    Set Username  merja
    Set Password  merjamerjanen
    Set Password Confirmation  merjamerjanen
    Submit Credentials
    Register Should Fail With Message  Password cannot contain only letters  

Register With Nonmatching Password And Password Confirmation
    Set Username  merja
    Set Password  merja123
    Set Password Confirmation  merja456
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  jaakko
    Set Password  jaakko123
    Login
    Login Should Succeed

Login After Failed Registration
    Set Username  jaaGGima46_:D
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Register Should Fail With Message  Username must contain only lowercase letters
    Go To Login Page
    Set Username  jaaGGima46_:D
    Set Password  jaakko123
    Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register
