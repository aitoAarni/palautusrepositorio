*** Settings ***
Resource  resource.robot


*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Successful Registeration
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password}
    Submit Credentials

Failed Registeration
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password}
    Submit Credentials