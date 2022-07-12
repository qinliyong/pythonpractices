'''
xivak-notuk-cupad-tarek-zesuk-zupid-taryk-zesak-cined-tetuk-nasuk-zoryd-tirak-zysek-zaryd-tyrik-nisyk-nenad-tituk-nysil-hepyd-tovak-zutik-cepyd-toral-husol-henud-titak-hesak-nyrud-tarik-netak-zapad-tupek-hysek-zuned-tytyk-zisuk-hyped-tymik-hysel-hepad-tomak-zysil-nunad-tytak-nirik-copud-tevok-zasyk-nypud-tyruk-niryk-henyd-tityk-zyral-nyred-taryk-zesek-corid-tipek-zysek-nunad-tytal-hitul-hepod-tovik-zurek-hupyd-tavil-hesuk-zined-tetuk-zatel-hopod-tevul-haruk-cupod-tavuk-zesol-ninid-tetok-nasyl-hopid-teryl-nusol-heped-tovuk-hasil-nenod-titek-zyryl-hiped-tivyk-cosok-zorud-tirel-hyrel-hinid-tetok-hirek-zyped-tyrel-hitul-nyrad-tarak-hotok-cuvux
'''
'''Bubble Babble Binary Data Encoding是由Antti Huima创建的一种编码方法，可以把二进制信息表示为由交替的元音和辅音组成的伪词（pseudo-words），主要用于密码指纹，其编码也具有内置的纠错和冗余。编码格式每5个字符中间以-来分隔，作者的原意就是想把难以记得的二进制数据表示为难忘的伪词。
特征：Notice the encoding always begins & ends with "x" 以x开头结尾，5字符一组，-分隔
'''

from bubblepy import BubbleBabble

s = 'xivak-notuk-cupad-tarek-zesuk-zupid-taryk-zesak-cined-tetuk-nasuk-zoryd-tirak-zysek-zaryd-tyrik-nisyk-nenad-tituk-nysil-hepyd-tovak-zutik-cepyd-toral-husol-henud-titak-hesak-nyrud-tarik-netak-zapad-tupek-hysek-zuned-tytyk-zisuk-hyped-tymik-hysel-hepad-tomak-zysil-nunad-tytak-nirik-copud-tevok-zasyk-nypud-tyruk-niryk-henyd-tityk-zyral-nyred-taryk-zesek-corid-tipek-zysek-nunad-tytal-hitul-hepod-tovik-zurek-hupyd-tavil-hesuk-zined-tetuk-zatel-hopod-tevul-haruk-cupod-tavuk-zesol-ninid-tetok-nasyl-hopid-teryl-nusol-heped-tovuk-hasil-nenod-titek-zyryl-hiped-tivyk-cosok-zorud-tirel-hyrel-hinid-tetok-hirek-zyped-tyrel-hitul-nyrad-tarak-hotok-cuvux'

#a = BubbleBabble().decode(s)
a = 'xivak-norok-norad-tipol-norol-nipid-tisuk-zotak-nurud-tesil-nitok-hepod-torek-cesuk-coryd-tinak-zorik-nined-tomyl-nosal-hopid-tuvuk-zomek-zupod-tovuk-zumak-zoryd-tipuk-nyruk-zepyd-tonuk-zasol-nunud-tenok-nuvyl-nevax'
#b = BubbleBabble().decode(a)
b = 'ximil-hynyk-rotil-rytek-masal-folif-cysuh-zoboh-zobol-himok-dosyf-fizyx'
c = BubbleBabble().decode(b)
#bugku{th1s_1s_A_Bubb13}
print(a)
print(b)
print(c)