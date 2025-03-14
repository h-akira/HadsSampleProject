import os
MAPPING_PATH = "stage-01"  # API Gatewayをそのまま使う場合はステージ名、独自ドメインを使う場合は空文字列、Localでは空文字列に上書き
MAPPING_PATH_LOCAL = ""  # API Gatewayをそのまま使う場合はステージ名、独自ドメインを使う場合は空文字列、Localでは空文字列に上書き
DEBUG = True
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_URL = "/static"  # 先頭の/はあってもなくても同じ扱

# ログイン周りの設定
from hads.authenticate import Cognito, ManagedAuthPage
import boto3
if os.path.exists(os.path.join(BASE_DIR, "../admin.json")):
  import json
  with open(os.path.join(BASE_DIR, "../admin.json")) as f:
    admin = json.load(f)
  kwargs = {}
  try:
    kwargs["region_name"] = admin["region"]
  except KeyError:
    pass
  try:
    kwargs["profile_name"] = admin["profile"]
  except KeyError:
    pass
  session = boto3.Session(**kwargs)
  ssm = session.client('ssm')
else:
  ssm = boto3.client('ssm')
COGNITO= Cognito(
  domain = ssm.get_parameter(Name="/HadsSampleProject/Cognito/domain")["Parameter"]["Value"],
  user_pool_id = ssm.get_parameter(Name="/HadsSampleProject/Cognito/user_pool_id")["Parameter"]["Value"],
  client_id = ssm.get_parameter(Name="/HadsSampleProject/Cognito/client_id")["Parameter"]["Value"],
  client_secret = ssm.get_parameter(Name="/HadsSampleProject/Cognito/client_secret")["Parameter"]["Value"],
  region = "ap-northeast-1"
)
AUTH_PAGE = ManagedAuthPage(
  scope = "aws.cognito.signin.user.admin email openid phone",
  login_redirect_uri = ssm.get_parameter(Name="/HadsSampleProject/APIGW_URL")["Parameter"]["Value"],
  local_login_redirect_uri = "http://localhost:3000"
)

