# Character Alias Mapping Table (Hump-style Naming, no underline)
character_map = {
    # ===== 班纳特家族 =====
    # 父母（严格区分夫妇）
    'Mr. Bennet': 'MrBennet',
    'Mrs. Bennet': 'MrsBennet',
    'Bennet': 'MrBennet',  # 单独出现默认指父亲

    # 女儿们（长幼顺序）
    'Lizzy': 'Elizabeth',
    'Eliza': 'Elizabeth',
    'Miss Elizabeth': 'Elizabeth',
    'Miss Bennet (Elizabeth)': 'Elizabeth',  # 明确指伊丽莎白时

    'Jane': 'Jane',
    'Miss Bennet': 'Jane',  # 默认指长女简
    'Miss Jane Bennet': 'Jane',

    'Mary': 'Mary',
    'Miss Mary Bennet': 'Mary',

    'Kitty': 'Kitty',
    'Catherine Bennet': 'Kitty',
    'Miss Catherine': 'Kitty',

    'Lydia': 'Lydia',
    'Miss Lydia Bennet': 'Lydia',

    # ===== 达西相关 =====
    'Mr. Darcy': 'Darcy',
    'Fitzwilliam Darcy': 'Darcy',
    'Colonel Fitzwilliam': 'Fitzwilliam',  # 达西的表哥

    # ===== 宾利家族 =====
    'Mr. Bingley': 'Bingley',
    'Charles Bingley': 'Bingley',

    'Caroline Bingley': 'Caroline',
    'Miss Bingley': 'Caroline',

    'Mrs. Hurst': 'MrsHurst',
    'Louisa Hurst': 'MrsHurst',

    # ===== 其他关键角色 =====
    'Mr. Collins': 'Collins',
    'William Collins': 'Collins',

    'Charlotte Lucas': 'Charlotte',
    'Miss Lucas': 'Charlotte',

    'Lady Catherine': 'LadyCatherine',
    'Lady Catherine de Bourgh': 'LadyCatherine',

    'Mr. Wickham': 'Wickham',
    'George Wickham': 'Wickham',

    'Sir William Lucas': 'SirWilliam',

    # ===== 次要角色 =====
    'Mr. Hurst': 'Hurst',
    'Maria Lucas': 'Maria',
    'Mr. Gardiner': 'Gardiner',
    'Mrs. Gardiner': 'MrsGardiner'
}

# 配套阵营分类（同步修改命名）
CHARACTER_TEAMS = {
    'MrBennet': '正派',
    'MrsBennet': '中性',
    'Elizabeth': '正派',
    'Jane': '正派',
    'Darcy': '正派',
    'Bingley': '正派',
    'Wickham': '反派',
    'LadyCatherine': '反派',
    'Collins': '反派',
    'Caroline': '反派',
    'MrsHurst': '反派'
}