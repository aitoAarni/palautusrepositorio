*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  tomppa
    Set Password  tomppa22
    Set Password Confirmation  tomppa22
    Submit Credentials
    Registeration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  to
    Set Password  tomppa22
    Set Password Confirmation  tomppa22
    Submit Credentials
    Registeration Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  tomppa
    Set Password  tomp22
    Set Password Confirmation  tomp22
    Submit Credentials
    Registeration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  tomppa
    Set Password  tomppa22
    Set Password Confirmation  tomppa23
    Submit Credentials
    Registeration Should Fail With Message  Passwords don't match

Login After Successful Registration
    Successful Registeration  tomppa  tomppa22
    Go To Login Page
    Set Username  tomppa
    Set Password  tomppa22
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Failed Registeration  he  mbappe
    Go To Login Page
    Set Username  tomppa
    Set Password  tomppa22
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Registeration Should Succeed
    Welcome Page Should Be Open

Registeration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Create User And Go To Register Page
    Create User  kalevi  kalevi08
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}
