def get():
    import random
    NAMES = [
        'albattani',
        'allen',
        'almeida',
        'agnesi',
        'archimedes',
        'ardinghelli',
        'aryabhata',
        'austin',
        'babbage',
        'banach',
        'bardeen',
        'bartik',
        'bassi',
        'beaver',
        'bell',
        'benz',
        'bhabha',
        'bhaskara',
        'blackwell',
        'bohr',
        'booth',
        'borg',
        'bose',
        'boyd',
        'brahmagupta',
        'brattain',
        'brown',
        'carson',
        'chandrasekhar',
        'chaplygin',
        'chatterjee',
        'chebyshev',
        'shannon',
        'clarke',
        'colden',
        'cori',
        'cray',
        'curran',
        'curie',
        'darwin',
        'davinci',
        'dijkstra',
        'dubinsky',
        'easley',
        'edison',
        'einstein',
        'elion',
        'elbakyan',
        'engelbart',
        'euclid',
        'euler',
        'fermat',
        'fermi',
        'feynman',
        'franklin',
        'galileo',
        'gates',
        'goldberg',
        'goldstine',
        'goldwasser',
        'golick',
        'goodall',
        'haibt',
        'hamilton',
        'hawking',
        'heisenberg',
        'hermann',
        'heyrovsky',
        'hodgkin',
        'hoover',
        'hopper',
        'hugle',
        'hypatia',
        'jackson',
        'jang',
        'jennings',
        'jepsen',
        'johnson',
        'joliot',
        'jones',
        'kalam',
        'kapitsa',
        'kare',
        'keldysh',
        'keller',
        'kepler',
        'khorana',
        'kilby',
        'kirch',
        'knuth',
        'kowalevski',
        'lalande',
        'lamarr',
        'lamport',
        'leakey',
        'leavitt',
        'lewin',
        'lichterman',
        'liskov',
        'lovelace',
        'lumiere',
        'mahavira',
        'mayer',
        'mccarthy',
        'mcclintock',
        'mclean',
        'mcnulty',
        'mendeleev',
        'meitner',
        'meninsky',
        'mestorf',
        'minsky',
        'mirzakhani',
        'morse',
        'murdock',
        'neumann',
        'newton',
        'nightingale',
        'nobel',
        'noether',
        'northcutt',
        'noyce',
        'panini',
        'pare',
        'pasteur',
        'payne',
        'perlman',
        'pike',
        'poincare',
        'poitras',
        'proskuriakova',
        'ptolemy',
        'raman',
        'ramanujan',
        'ride',
        'montalcini',
        'ritchie',
        'roentgen',
        'rosalind',
        'saha',
        'sammet',
        'shaw',
        'shirley',
        'shockley',
        'sinoussi',
        'snyder',
        'spence',
        'stallman',
        'shtern',
        'stonebraker',
        'swanson',
        'swartz',
        'swirles',
        'tereshkova',
        'tesla',
        'thompson',
        'torvalds',
        'turing',
        'varahamihira',
        'vaughan',
        'visvesvaraya',
        'volhard',
        'villani',
        'wescoff',
        'wiles',
        'williams',
        'wilson',
        'wing',
        'wozniak',
        'wright',
        'yalow',
        'yonath',
        'zhukovsky',
    ]

    ADJECTIVES = [
        'admiring',
        'adoring',
        'affectionate',
        'agitated',
        'amazing',
        'angry',
        'awesome',
        'blissful',
        'boring',
        'brave',
        'clever',
        'cocky',
        'compassionate',
        'competent',
        'condescending',
        'confident',
        'cranky',
        'dazzling',
        'determined',
        'distracted',
        'dreamy',
        'eager',
        'ecstatic',
        'elastic',
        'elated',
        'elegant',
        'eloquent',
        'epic',
        'fervent',
        'festive',
        'flamboyant',
        'focused',
        'friendly',
        'frosty',
        'gallant',
        'gifted',
        'goofy',
        'gracious',
        'happy',
        'hardcore',
        'heuristic',
        'hopeful',
        'hungry',
        'infallible',
        'inspiring',
        'jolly',
        'jovial',
        'keen',
        'kind',
        'laughing',
        'loving',
        'lucid',
        'mystifying',
        'modest',
        'musing',
        'naughty',
        'nervous',
        'nifty',
        'nostalgic',
        'objective',
        'optimistic',
        'peaceful',
        'pedantic',
        'pensive',
        'practical',
        'priceless',
        'quirky',
        'quizzical',
        'relaxed',
        'reverent',
        'romantic',
        'sad',
        'serene',
        'sharp',
        'silly',
        'sleepy',
        'stoic',
        'stupefied',
        'suspicious',
        'tender',
        'thirsty',
        'trusting',
        'unruffled',
        'upbeat',
        'vibrant',
        'vigilant',
        'vigorous',
        'wizardly',
        'wonderful',
        'xenodochial',
        'youthful',
        'zealous',
        'zen',
    ]
    return random.choice(ADJECTIVES) + "-" + random.choice(NAMES)