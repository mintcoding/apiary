# Apiary

This system imports disturbance as a python package (see requirements.txt)

# Requirements

- Python (2.7.x)
- PostgreSQL (>=9.3)

Python library requirements should be installed using `pip`:

`pip install -r requirements.txt`

# Environment settings

A `.env` file should be created in the project root and used to set
required environment variables at run time. Example content:

    DEBUG=True
    SECRET_KEY='thisismysecret'
    DATABASE_URL='postgis://USER:PASSWORD@HOST:PORT/DB_NAME'
    ALLOWED_HOSTS=[u'das.domain.com.au',u'das-internal.domain.com.au']
    EMAIL_HOST='EMAIL_HOST'
    BPOINT_USERNAME='BPOINT_USER'
    BPOINT_PASSWORD='BPOINT_PW'
    BPOINT_BILLER_CODE='123456'
    BPOINT_MERCHANT_NUM='987654'
    BPAY_BILLER_CODE='121212'
    CMS_URL="https://url-used-to-retrieve-system-id-via-api/"
    LEDGER_USER="UserForSystemIdAPI"
    LEDGER_PASS="Password"
    OSCAR_SHOP_NAME='Shop 1'
    DEFAULT_FROM_EMAIL='system@email_address.com.au'
    NOTIFICATION_EMAIL='user.notification@email_address.com.au'
    NON_PROD_EMAIL='user_1@email_address.com.au,user_2@email_address.com.au'
    EMAIL_INSTANCE='DEV/TEST/UAT/PROD'
    PRODUCTION_EMAIL=False
    BPAY_ALLOWED=False
    LEDGER_GST=10
    SITE_PREFIX='das'
    SITE_DOMAIN='domain.com.au
