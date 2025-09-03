# XML标签翻译映射
TAG_TRANSLATIONS = {
    # 根标签
    'Document': '文档',

    # 产品结果
    'ProductResults': '产品结果',
    'OrgQryID': '机构查询ID',
    'FbMsg': '反馈消息',
    'OrgCode': '机构代码',

    # 产品信息
    'Product': '产品',

    # 产品头部信息
    'PdctHdr': '产品头部',
    'PdctBsicInf': '产品基本信息',
    'InstnTp': '机构类型',
    'PdctTp': '产品类型',
    'PdctVrsn': '产品版本',
    'FormTm': '形成时间',
    'EntCertTp': '企业证件类型',
    'ProvideDt': '提供日期',

    # 基本信息
    'BsicInf': '基本信息',
    'Id': '标识',
    'EntNm': '企业名称',
    'EntId': '企业ID',
    'EntIdTp': '企业ID类型',
    'EntIdCode': '企业ID代码',
    'FinAcctLSD': '金融账户最后四位',

    # 支付信用信息
    'PmtCdtInf': '支付信用信息',
    'DataLabl': '数据标签',

    # 资本概况
    'CptlPrfl': '资本概况',

    # 资本状况
    'CptStat': '资本状况',
    'CptStatCounts': '资本状况计数',
    'CptStatDtls': '资本状况详情',
    'CcyTp': '货币类型',
    'OcrdTm': '发生时间',
    'IncmAmt': '收入金额',
    'IncmTxs': '收入交易数',
    'ExpndtrAmt': '支出金额',
    'ExpndtrTxs': '支出交易数',
    'DalyAvrgOfMnth': '月日均',
    'EndofMnth': '月末余额',
    'DalyAvrgOfQrtr': '季日均',

    # 资本现金
    'CptCash': '资本现金',
    'CptCashCounts': '资本现金计数',
    'CptCashDtls': '资本现金详情',
    'DpstAmt': '存款金额',
    'DpstTxs': '存款交易数',
    'DpstIncmRate': '存款收入率',
    'WdrwAmt': '取款金额',
    'WdrwTxs': '取款交易数',
    'WdrwExpndtrRate': '取款支出率',
    'NetgRate': '净率',

    # 机构交易
    'InstnTx': '机构交易',
    'InstnTxCounts': '机构交易计数',

    # 同企业交易
    'SameEnTx': '同企业交易',
    'SameEnTxCounts': '同企业交易计数',

    # 第三方交易
    'ThrdPtyTx': '第三方交易',
    'ThrdPtyTxCounts': '第三方交易计数',

    # 代理交易
    'AgtTx': '代理交易',
    'AgtTxCounts': '代理交易计数',

    # 内部代理交易
    'IntraAgtTx': '内部代理交易',
    'IntraAgtTxCounts': '内部代理交易计数',
    'IntraAgtTxDtls': '内部代理交易详情',
    'TxTp': '交易类型',
    'TradTp': '贸易类型',

    # 其他交易
    'OthrTx': '其他交易',
    'OthrInstnTxCounts': '其他机构交易计数',
    'OthrInstnTxDtls': '其他机构交易详情',
    'IncmContraCounts': '收入对手计数',
    'ExpndtrContraCounts': '支出对手计数',

    # 最大金额
    'BiggestAmt': '最大金额',
    'BiggestAmtCounts': '最大金额计数',
    'BiggestAmtDtls': '最大金额详情',

    # 交易集中度
    'TxnlCncntrtn': '交易集中度',
    'TxnlCncntrtnCounts': '交易集中度计数',
    'TxnlCncntrtnDtls': '交易集中度详情',
    'CtrPty': '交易对手',

    # 交易分布
    'TxnlDstrbtn': '交易分布',
    'TxnlDstrbtnCounts': '交易分布计数',
    'TxnlDstrbtnDtls': '交易分布详情',
    'CtrPtiesCountsOfIncm': '收入对手计数',
    'CtrPtiesCountsOfExpndtr': '支出对手计数',
    'AvrgIncmAmt': '平均收入金额',
    'AvrgExpndtrAmt': '平均支出金额',

    # 交易稳定性
    'TxnlStability': '交易稳定性',
    'TxnlStabilityCounts': '交易稳定性计数',
    'TxnlStabilityDtls': '交易稳定性详情',
    'AbovOneCtrPtiesCountsOfIncm': '收入多对手计数',
    'AbovOneCtrPtiesCountsOfExpndtr': '支出多对手计数',

    # 交易周转率
    'TxnlTrnvrRate': '交易周转率',
    'TxnlTrnvrRateCounts': '交易周转率计数',
    'TxnlTrnvrRateDtls': '交易周转率详情',

    # 交易趋势
    'TxnlTrend': '交易趋势',
    'TxnlTrendCounts': '交易趋势计数',
    'TxnlTrendDtls': '交易趋势详情',
    'Fltg': '浮动',
    'MnthsCountsOfIncm': '收入月数',
    'MnthsCountsOfExpndtr': '支出月数',
    'AvrgTxsOfIncm': '平均收入交易数',

    # 金额区域分布
    'DvdAmtRgn': '金额区域分布',
    'DvdAmtRgnCounts': '金额区域分布计数',
    'DvdAmtRgnDtls': '金额区域分布详情',
    'AmtRgn': '金额区域',

    # 产品附加信息
    'ProductAddtnInfo': '产品附加信息',
    'IsObjct': '是否客观',
    'IsStmt': '是否声明',
    'QryID': '查询ID',
    'IsFinAcctClosed': '金融账户是否关闭'
}


def get_tag_translation(tag_name):
    """
    获取标签的中文翻译

    Args:
        tag_name (str): 标签名

    Returns:
        str: 标签的中文翻译，如果未找到则返回原标签名
    """
    return TAG_TRANSLATIONS.get(tag_name, tag_name)


def translate_tag_hierarchy(hierarchy_dict):
    """
    翻译标签层级结构

    Args:
        hierarchy_dict (dict): 标签层级字典

    Returns:
        dict: 翻译后的标签层级字典
    """
    translated = {}
    for tag, children in hierarchy_dict.items():
        translated_tag = get_tag_translation(tag)
        if isinstance(children, dict) and children:
            translated[translated_tag] = translate_tag_hierarchy(children)
        else:
            translated[translated_tag] = children
    return translated


# 使用示例
if __name__ == '__main__':
    # 示例：翻译单个标签
    print("标签翻译示例:")
    test_tags = ['Product', 'BsicInf', 'EntNm', 'CptStatDtls', 'IncmAmt']
    for tag in test_tags:
        print(f"{tag} -> {get_tag_translation(tag)}")

    print("\n完整标签翻译映射已定义，可直接使用。")
