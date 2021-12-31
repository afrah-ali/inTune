books_to_music = {
    'romance': ['dreamy', 'elegant', 'hopeful', 'romantic', 'sensual', 'euphoric'],
    'gritty': ['gritty', 'dark', 'gothic', 'urban'],
    'epic': ['epic', 'coming-of-age', 'battle', 'hopeful', 'adventurous', 'tragedy', 'stressed'],
    'gothic': ['gothic', 'eerie', 'dark-academia', 'witchy'],
    'dark-academia': ['dark-academia', 'gothic', 'introspective', 'melancholic', 'coming-of-age'],
    'light-academia': ['light-academia', 'slice-of-life', 'peaceful', 'eccentric'],
    'introspective': ['introspective', 'coming-of-age', 'sentimental'],
    'young-adult': ['coming-of-age', 'sentimental'],
    'fantasy': ['elegant', 'epic', 'adventurous', 'ethereal', 'battle'],
    'science-fiction': ['dreamy', 'eccentric', 'cyber-punk'],
    'children': ['eccentric', 'slice-of-life', 'peaceful'],
    'historical-fiction': ['elegant', 'introspective', 'sentimental', 'melancholic'],
    'mystery': ['mystery', 'stressed', 'melancholic', 'suspense'],
    'horror': ['eerie', 'suspense', 'tragedy', 'dark', 'gothic'],
    'paranormal': ['eerie', 'suspense', 'supernatural', 'tragedy'], 
    'historical-romance': ['elegant', 'introspective', 'sentimental', 'melancholic', 'hopeful', 'romantic', 'sensual', 'euphoric'],
    'thriller': ['eerie', 'gritty', 'mystery', 'suspense', 'thriller'],
    'contemporary': ['slice-of-life', 'peaceful', 'light-academia', 'glamorous'],
    'classics': ['elegant', 'epic', 'coming-of-age', 'introspective', 'sentimental'],
    'crime': ['gritty', 'thriller', 'dark', 'suspense', 'urban'],
    'humor': ['dreamy', 'eccentric', 'slice-of-life', 'light-academia'],
    'suspense':['suspense', 'mystery', 'gritty', 'dark'],
    'dystopia': ['gritty', 'dark', 'dystopia', 'melancholic', 'urban', 'cyber-punk'],
    'adventure': ['epic', 'hopeful', 'battle', 'adventurous', 'coming-of-age'],
    'african-american': ['sentimental', 'introspective', 'melancholic', 'urban'],
    'asian-literature': ['elegant', 'sentimental', 'introspective', 'melancholic'],
    'biblical-fiction': ['elegant', 'euphoric', 'dreamy', 'hopeful', 'epic', 'sentimental', 'introspective', 'ethereal'],
    'chick-lit': ['eccentric', 'slice-of-life', 'romantic', 'sensual', 'sentimental', 'glamorous'],
    'christian-fiction': ['elegant', 'euphoric', 'dreamy', 'hopeful', 'epic', 'sentimental', 'introspective', 'ethereal', 'peaceful'],
    'civil-war': ['dark', 'tragedy', 'melancholic', 'hopeful', 'battle', 'sentimental', 'elegant'],
    'cyberpunk': ['gritty', 'urban', 'cyberpunk', 'eccentric', 'dreamy', 'dystopia', 'glamorous'],
    'dark': ['gritty', 'dark', 'melancholic', 'dark-academia'],
    'drama': ['stressed', 'romantic', 'sensual', 'sentimental', 'introspective'],
    'fantasy-romance': ['elegant', 'epic', 'adventurous', 'ethereal', 'battle', 'romantic', 'sensual', 'sentimental', 'melancholic'],
    'folklore': ['epic', 'dreamy', 'battle', 'coming-of-age', 'hopeful', 'sentimental', 'peaceful'],
    'french-literature': ['elegant', 'introspective', 'sentimental', 'melancholic'],
    'high-school': ['eccentric', 'slice-of-life', 'hopeful', 'coming-of-age'],
    historical-mystery
    latin-american-literature
    legal-thriller
    gay-fiction
    lesbian-fiction
    lgbt
    literary-fiction
    high-fantasy
    low-fantasy
    lovecraftian
    urban-fantasy
    supernatural
    futuristic
    magic
    medieval
    military-fiction
    modern-classics
    mystery-thriller
    mythology
    psychological-thriller
    pulp-noir
    punk
    realistic-fiction
    regency-romance
    russian-literature
    romantic-suspense
    slice-of-life
    space-opera
    steampunk
    spy-thriller
    sports-romance
    supernatural-romance
    time-travel
    tragedy
    victorian
    westerns
    world-war-i
    world-war-ii
}

'''
1. gritty
2. eerie
3. dystopia
4. dark
5. dreamy
6. eccentric
7. elegant
8. epic
9. euphoric
10. adventurous
11. slice of life
13. thriller
14. ethereal
15. gothic
16. light academia - optimism, sensitivity, joy, gratitude, friendship, motivation, and happy endings
17. glamourous
18. introspective
19. hopeful
20. tragedy
21. coming of age
23. battle
24. mystery
25. peaceful
26. stressed
27. romantic
28. melancholy
29. sentimental
30. sad
31. sensual
32. suspense
33. urban
35. cyber-punk
36. supernatural
37. witchy
38. dark academia - literary tragedy, discussion of the meaning of life, heartbreak, oppression, escapism, and death
'''
def returntags():
    return '''romance
    gritty
    epic
    gothic
    dark-academia
    light-academia
    introspective
    young-adult
    fantasy
    science-fiction
    children
    historical-fiction
    mystery
    horror
    gay
    paranormal
    historical-romance
    thriller
    contemporary
    classics
    crime
    humor
    suspense
    dystopia
    adventure
    african-american
    asian-literature
    biblical-fiction
    chick-lit
    christian-fiction
    civil-war
    cyberpunk
    dark
    drama
    fantasy-romance
    folklore
    french-literature
    high-school
    historical-mystery
    latin-american-literature
    legal-thriller
    gay-fiction
    lesbian-fiction
    lgbt
    literary-fiction
    high-fantasy
    low-fantasy
    lovecraftian
    urban-fantasy
    supernatural
    futuristic
    magic
    medieval
    military-fiction
    modern-classics
    mystery-thriller
    mythology
    psychological-thriller
    pulp-noir
    punk
    queer-lit
    realistic-fiction
    regency-romance
    russian-literature
    romantic-suspense
    slice-of-life
    space-opera
    steampunk
    spy-thriller
    sports-romance
    supernatural-romance
    time-travel
    tragedy
    victorian
    westerns
    world-war-i
    world-war-ii'''.replace("   ", "").replace(" ", "").split("\n")