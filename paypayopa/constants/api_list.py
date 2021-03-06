class API_NAMES(object):
    CANCEL_PAYMENT = "v2_cancelPayment"
    CAPTURE_PAYMENT = "v2_captureAuthorizedOrder"
    CREATE_PAYMENT = "v2_createPayment"
    CREATE_QRCODE = "v2_createDynamicQRCode"
    DELETE_QRCODE = "v2_deleteDynamicQRCode"
    GET_PAYMENT = "v2_getPaymentDetail"
    GET_QR_PAYMENT = "v2_getQRPaymentDetails"
    GET_REFUND = "v2_getRefundDetails"
    REFUND_PAYMENT = "v2_createRefundPayment"
    REVERT_AUTHORIZE = "v2_revertAuthorizedOrder"
    PREAUTHORIZE_PAYMENT = "v2_createOrderAndAuthorize"
    CREATE_CONTINUOUS_PAYMENT = "v1_createSubscriptionPayment"
    CREATE_REQUEST_ORDER = "v1_createRequestOrder"
    GET_REQUEST_ORDER = "v1_getRequestOrder"
    CANCEL_REQUEST_ORDER = "v1_cancelRequestOrder"
    REFUND_REQUEST_ORDER = "v2_createRefundPayment"
    GET_SECURE_USER_PROFILE = "v2_getSecureUserProfile"
    CHECK_BALANCE = "v2_checkWalletBalance"
    GET_USER_AUTH_STATUS = "v2_userAuthStatus"
    UNLINK_USER = "v2_unlinkUser"
    CREATE_QR_SESSION = "v1_qrSession"
    CREATE_CASHBACK_REQUEST = "v2_createCashBackRequest" #GIVE_CASHBACK = 'v2_createRefundPayment'
    GET_CASHBACK_DETAILS = "v2_getCashbackDetails" #REVERSAL_CASHBACK = 'v2_reversalCashback'
    CREATE_REVERSE_CASHBACK_REQUEST = "v2_createReverseCashBackRequest"
    GET_REVERESED_CASHBACK_DETAILS = "v2_getReversedCashBackDetails"
