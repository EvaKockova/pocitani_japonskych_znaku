hiragana = '''ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみ
むもゃやゅゆょよらりるれろゎわゐゑをんゔ'''
katakana = '''ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ'''
pocet_znaku_hiragana = 0
pocet_znaku_katakana = 0

with open('rozsypany_caj.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()
    for znak in obsah:
        if znak in hiragana:
            pocet_znaku_hiragana = pocet_znaku_hiragana + 1
        elif znak in katakana:
            pocet_znaku_katakana = pocet_znaku_katakana + 1

    #for znak in hiragana:
    #    if znak in obsah:
    #        pocet_znaku_hiragana = pocet_znaku_hiragana + 1
    #for znak in katakana:
    #    if znak in obsah:
    #        pocet_znaku_katakana = pocet_znaku_katakana + 1

print('Počet znaků z hiragany je', pocet_znaku_hiragana, '.')
print('Počet znaků z katakany je', pocet_znaku_katakana, '.')
