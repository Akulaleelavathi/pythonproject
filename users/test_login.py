from settings.conftest import main_url,mobile_number
from users.users import send_otp,verify_otp,get_workspace
from users.mfa_login import verify_mobile_otp,verify_email_otp, get_workspacess
main_workspace = ""
main_token= ""
send_otp_response = send_otp(main_url,mobile_number)

if send_otp_response["mfaStatus"]:
    # print(otp_res)
    verify_mobile_res = verify_mobile_otp(send_otp_response,mobile_number, main_url)
    # print(verify_mobile_res)
    verify_email_res = verify_email_otp(send_otp_response, verify_mobile_res, main_url)
    main_token = verify_email_res["token"]
    get_workspaces = get_workspacess(verify_email_res, main_url)
    main_workspace = get_workspaces

else:
    token = verify_otp(send_otp_response,main_url,mobile_number)
    main_token = token
    workspace = get_workspace(token,main_url)
    main_workspace = workspace

# print(main_workspace)
# print(len(main_workspace))
# print(main_token)