
print('Ця програма призначена для перевірки знань з української мови. Ця версія призначена лише для слів, що складаються з 3 або 4 букв. ')
while True:

    word= input('Введіть, будь ласка, слово. Якщо бажаєте зупинити програму напишіть слово (stop) ')
    if word == "stop": break
    nah=input('На яку букву падає наголос ')
    wordbreak=list(word)
    long=len(word)
    print(wordbreak)
    if long==3:
        col1=word[0]
        col2=word[1]
        col3=word[2]
        if col1=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col1=='б':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[б]- приголосний, дзвінкий, '+ mah +'.')
        elif col1=='в':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[в]- приголосний, сонорний, ' + mah +'.')
        elif col1=='г':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний, дзінкий, ' + mah +'.')
        elif col1=='г':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний, дзвінкий, '+ mah +'.')
        elif col1=='д':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[д]- приголосний, дзвінкий, '+ mah +'.')
        elif col1=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний, '+ nah2)
        elif col1=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний, сонорний,')
            print ('[е]- голосний, ' + nah3)
        elif col1=='ж':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ж]- приголосний, дзвінкий, '+ mah +'.')
        elif col1=='з':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[з]- приголосний, дзвінкий, '+ mah +'.')
        elif col1=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний, ' + nah4)
        elif col1=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний, '+ nah5)
        elif col1=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний, сонорний, ')
            print ('[і]- голосний, ' + nah6)
        elif col1=='й':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[й]- приголосний, сонорний, ')
        elif col1=='к':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[к]- приголосний, глухий, '+ mah +'.')
        elif col1=='л':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[л]- приголосний, сонорний '+ mah +'.')
        elif col1=='м':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[м]- приголосний, сонорний, '+ mah +'.')
        elif col1=='н':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[н]- приголосний, сонорний, '+ mah +'.')
        elif col1=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний, ' + nah6)
        elif col1=='п':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[п]- приголосний, глухий, ' + mah +'.')
        elif col1=='р':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[р]- приголосний, сонорний, '+ mah +'.')
        elif col1=='с':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[с]- приголосний, глухий, '+ mah +'.')
        elif col1=='т':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[т]- приголосний, глухий, '+ mah +'.')
        elif col1=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний, '+ nah7)
        elif col1=='ф':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ф]- приголосний, глухий, '+ mah +'.')
        elif col1=='х':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[х]- приголосний, глухий, '+ mah +'.')
        elif col1=='ц':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ц]- приголосний, глухий, '+ mah +'.')
        elif col1=='ч':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ч]- приголосний, глухий, '+ mah +'.')
        elif col1=='ш':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ш]- приголосний, глухий, '+ mah +'.')
        elif col1=='щ':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[щ]- приголосний, глухий '+ mah +'.')
        elif col1=='ь':
            print (' ')
        elif col1=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний, сонорний,')
            print ('[у]- голосний,' + nah8)
        elif col1=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний, сонорний,')
            print ('[а]- голосний, ' +nah9)
        if col2=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col2=='б':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[б]- приголосний, дзвінкий, '+ mah +'.')
        elif col2=='в':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[в]- приголосний,сонорний, ' + mah +'.')
        elif col2=='г':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний, дзінкий, ' + mah +'.')
        elif col2=='г':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний, дзвінкий, '+ mah +'.')
        elif col2=='д':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[д]- приголосний, дзвінкий, '+ mah +'.')
        elif col2=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний, '+ nah2)
        elif col2=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний, сонорний,')
            print ('[е]- голосний, ' + nah3)
        elif col2=='ж':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ж]- приголосний, дзвінкий, '+ mah +'.')
        elif col2=='з':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[з]- приголосний, дзвінкий,'+ mah +'.')
        elif col2=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний, ' + nah4)
        elif col2=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний, '+ nah5)
        elif col2=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний, сонорний, ')
            print ('[і]- голосний,' + nah6)
        elif col2=='й':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[й]- приголосний,сонорний, ')
        elif col2=='к':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[к]- приголосний, глухий, '+ mah +'.')
        elif col2=='л':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[л]- приголосний, сонорний, '+ mah +'.')
        elif col2=='м':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[м]- приголосний, сонорний, '+ mah +'.')
        elif col2=='н':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[н]- приголосний, сонорний, '+ mah +'.')
        elif col2=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний, ' + nah6)
        elif col2=='п':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[п]- приголосний, глухий, '+ mah +'.')
        elif col2=='р':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[р]- приголосний, сонорний, '+ mah +'.')
        elif col2=='с':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[с]- приголосний, глухий, '+ mah +'.')
        elif col2=='т':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[т]- приголосний, глухий, '+ mah +'.')
        elif col2=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний, '+ nah7)
        elif col2=='ф':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ф]- приголосний, глухий, '+ mah +'.')
        elif col2=='х':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[х]- приголосний, глухий, '+ mah +'.')
        elif col2=='ц':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ц]- приголосний, глухий, '+ mah +'.')
        elif col2=='ч':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ч]- приголосний, глухий, '+ mah +'.')
        elif col2=='ш':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ш]- приголосний, глухий, '+ mah +'.')
        elif col2=='щ':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[щ]- приголосний, глухий '+ mah +'.')
        elif col2=='ь':
            print (' ')
        elif col2=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний, сонорний, ')
            print ('[у]- голосний,' + nah8)
        elif col2=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний, сонорний, ')
            print ('[а]- голосний,' +nah9)


        if col3=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col3=='б':
            print ('[б]- приголосний, дзвінкий, твердий')
        elif col3=='в':
            print ('[в]- приголосний, сонорний, твердий.')
        elif col3=='г':
            print ('[г]- приголосний, дзвінкий, твердий')
        elif col3=='г':
            print ('[г]- приголосний, дзвінкий, твердий')
        elif col3=='д':
            print ('[д]- приголосний, дзвінкий, твердий')
        elif col3=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний,'+ nah2)
        elif col3=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний, сонорний, твердий.')
            print ('[е]- голосний,' + nah3)
        elif col3=='ж':
            print ('[ж]- приголосний, дзвінкий, твердий.')
        elif col3=='з':
            print ('[з]- приголосний, дзвінкий, твердий.')
        elif col3=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний,' + nah4)
        elif col3=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний,'+ nah5)
        elif col3=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний, сонорний,.')
            print ('[і]- голосний,' + nah6)
        elif col3=='й':
            print ('[й]- приголосний, сонорний, твердий.')
        elif col3=='к':
            print ('[к]- приголосний, глухий, твердий.')
        elif col3=='л':
            print ('[л]- приголосний, сонорний, твердий.')
        elif col3=='м':
            print ('[м]- приголосний, сонорний, твердий.')
        elif col3=='н':
            print ('[н]- приголосний, сонорний, твердий.')
        elif col3=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний, ' + nah6)
        elif col3=='п':
            print ('[п]- приголосний, глухий, тваердий .')
        elif col3=='р':
            print ('[р]- приголосний, сонорний, твердий .')
        elif col3=='с':
            print ('[с]- приголосний, глухий, твердий.')
        elif col3=='т':
            print ('[т]- приголосний, глухий, твердий.')
        elif col3=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний,'+ nah7)
        elif col3=='ф':
            print ('[ф]- приголосний, глухий, твердий.')
        elif col3=='х':
            print ('[х]- приголосний, глухий, твердий.')
        elif col3=='ц':
            print ('[ц]- приголосний, глухий,твердий.')
        elif col3=='ч':
            print ('[ч]- приголосний, глухий, твердий .')
        elif col3=='ш':
            print ('[ш]- приголосний, глухий, твердий')
        elif col3=='щ':
            print ('[щ]- приголосний, глухий, твердий')
        elif col3=='ь':
            print (' ')
        elif col3=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний, сонорний, твердий.')
            print ('[у]- голосний, ' + nah8)
        elif col3=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний, сонорний, твердий.')
            print ('[а]- голосний,' +nah9)


    elif long==4:
        col1=word[0]
        col2=word[1]
        col3=word[2]
        col4=word[3]
        if col1=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col1=='б':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[б]- приголосний,дзвінкий,'+ mah +'.')
        elif col1=='в':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[в]- приголосний,сонорний,' + mah +'.')
        elif col1=='г':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний,дзінкий .' + mah +'.')
        elif col1=='г':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний,дзвінкий .'+ mah +'.')
        elif col1=='д':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[д]- приголосний,дзвінкий.'+ mah +'.')
        elif col1=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний,'+ nah2)
        elif col1=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний,сонорний,')
            print ('[е]- голосний,' + nah3)
        elif col1=='ж':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ж]- приголосний, дзвінкий.'+ mah +'.')
        elif col1=='з':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[з]- приголосний,дзвінкий.'+ mah +'.')
        elif col1=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний,' + nah4)
        elif col1=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний,'+ nah5)
        elif col1=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[і]- голосний,' + nah6)
        elif col1=='й':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[й]- приголосний,сонорний,.')
        elif col1=='к':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[к]- приголосний, глухий,'+ mah +'.')
        elif col1=='л':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[л]- приголосний,сонорний,'+ mah +'.')
        elif col1=='м':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[м]- приголосний,сонорний,'+ mah +'.')
        elif col1=='н':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[н]- приголосний,сонорний,'+ mah +'.')
        elif col1=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний,' + nah6)
        elif col1=='п':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[п]- приголосний,глухий,'+ mah +'.')
        elif col1=='р':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[р]- приголосний,сонорний,'+ mah +'.')
        elif col1=='с':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[с]- приголосний,глухий,'+ mah +'.')
        elif col1=='т':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[т]- приголосний, глухий,'+ mah +'.')
        elif col1=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний,'+ nah7)
        elif col1=='ф':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ф]- приголосний,глухий,'+ mah +'.')
        elif col1=='х':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[х]- приголосний,глухий,'+ mah +'.')
        elif col1=='ц':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ц]- приголосний,глухий,'+ mah +'.')
        elif col1=='ч':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ч]- приголосний,глухий,'+ mah +'.')
        elif col1=='ш':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ш]- приголосний,глухий,'+ mah +'.')
        elif col1=='щ':
            if col2=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[щ]- приголосний,глухий'+ mah +'.')
        elif col1=='ь':
            print (' ')
        elif col1=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[у]- голосний,' + nah8)
        elif col1=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[а]- голосний,' +nah9)
        if col2=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col2=='б':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[б]- приголосний,дзвінкий,'+ mah +'.')
        elif col2=='в':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[в]- приголосний,сонорний,' + mah +'.')
        elif col2=='г':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний,дзінкий .' + mah +'.')
        elif col2=='г':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний,дзвінкий .'+ mah +'.')
        elif col2=='д':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[д]- приголосний,дзвінкий.'+ mah +'.')
        elif col2=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний,'+ nah2)
        elif col2=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний,сонорний,')
            print ('[е]- голосний,' + nah3)
        elif col2=='ж':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ж]- приголосний, дзвінкий.'+ mah +'.')
        elif col2=='з':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[з]- приголосний,дзвінкий.'+ mah +'.')
        elif col2=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний,' + nah4)
        elif col2=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний,'+ nah5)
        elif col2=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[і]- голосний,' + nah6)
        elif col2=='й':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[й]- приголосний,сонорний,.')
        elif col2=='к':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[к]- приголосний, глухий.'+ mah +'.')
        elif col2=='л':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[л]- приголосний,сонорний,'+ mah +'.')
        elif col2=='м':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[м]- приголосний,сонорний,.'+ mah +'.')
        elif col2=='н':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[н]- приголосний,сонорний,.'+ mah +'.')
        elif col2=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний,' + nah6)
        elif col2=='п':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[п]- приголосний,глухий,'+ mah +'.')
        elif col2=='р':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[р]- приголосний,сонорний,'+ mah +'.')
        elif col2=='с':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[с]- приголосний,глухий,'+ mah +'.')
        elif col2=='т':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[т]- приголосний, глухий,'+ mah +'.')
        elif col2=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний,'+ nah7)
        elif col2=='ф':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ф]- приголосний,глухий,'+ mah +'.')
        elif col2=='х':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[х]- приголосний,глухий,'+ mah +'.')
        elif col2=='ц':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ц]- приголосний,глухий,'+ mah +'.')
        elif col2=='ч':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ч]- приголосний,глухий,'+ mah +'.')
        elif col2=='ш':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ш]- приголосний,глухий,'+ mah +'.')
        elif col2=='щ':
            if col3=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[щ]- приголосний,глухий'+ mah +'.')
        elif col2=='ь':
            print (' ')
        elif col2=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[у]- голосний,' + nah8)
        elif col2=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[а]- голосний,' +nah9)
        if col3=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col3=='б':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[б]- приголосний,дзвінкий,'+ mah +'.')
        elif col3=='в':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[в]- приголосний,сонорний,' + mah +'.')
        elif col3=='г':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний,дзінкий .' + mah +'.')
        elif col3=='г':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[г]- приголосний,дзвінкий .'+ mah +'.')
        elif col3=='д':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[д]- приголосний,дзвінкий.'+ mah +'.')
        elif col3=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний,'+ nah2)
        elif col3=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний,сонорний,')
            print ('[е]- голосний,' + nah3)
        elif col3=='ж':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ж]- приголосний, дзвінкий.'+ mah +'.')
        elif col3=='з':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[з]- приголосний,дзвінкий.'+ mah +'.')
        elif col3=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний,' + nah4)
        elif col3=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний,'+ nah5)
        elif col3=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[і]- голосний,' + nah6)
        elif col3=='й':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[й]- приголосний,сонорний,.')
        elif col3=='к':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[к]- приголосний, глухий.'+ mah +'.')
        elif col3=='л':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[л]- приголосний,сонорний, '+ mah +'.')
        elif col3=='м':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[м]- приголосний,сонорний,.'+ mah +'.')
        elif col3=='н':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[н]- приголосний,сонорний,.'+ mah +'.')
        elif col3=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний,' + nah6)
        elif col3=='п':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[п]- приголосний,глухий,'+ mah +'.')
        elif col3=='р':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[р]- приголосний,сонорний,'+ mah +'.')
        elif col3=='с':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[с]- приголосний,глухий,'+ mah +'.')
        elif col3=='т':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[т]- приголосний, глухий,'+ mah +'.')
        elif col3=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний,'+ nah7)
        elif col3=='ф':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ф]- приголосний,глухий,'+ mah +'.')
        elif col3=='х':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[х]- приголосний,глухий,'+ mah +'.')
        elif col3=='ц':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ц]- приголосний,глухий,'+ mah +'.')
        elif col3=='ч':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ч]- приголосний,глухий,'+ mah +'.')
        elif col3=='ш':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[ш]- приголосний,глухий,'+ mah +'.')
        elif col3=='щ':
            if col4=='ь':
                mah="м'який"
            else :
                mah= "твердий"
            print ('[щ]- приголосний,глухий'+ mah +'.')
        elif col3=='ь':
            print (' ')
        elif col3=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[у]- голосний,' + nah8)
        elif col3=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[а]- голосний,' +nah9)


        if col4=='а':
            if nah== 'a':
                nah1='наголошений'
            else:
                nah1='ненаголошений'
            print ('[a]- голосний, '+ nah1)
        elif col4=='б':
            print ('[б]- приголосний,дзвінкий,твердий')
        elif col4=='в':
            print ('[в]- приголосний,сонорний,твердий.')
        elif col4=='г':
            print ('[г]- приголосний,дзвінкий,твердий')
        elif col4=='г':
            print ('[г]- приголосний, дзвінкий,твердий')
        elif col4=='д':
            print ('[д]- приголосний,дзвінкий,твердий')
        elif col4=='е':
            if nah== 'е':
                nah2='наголошений'
            else:
                nah2='ненаголошений'
            print ('[е]- голосний,'+ nah2)
        elif col4=='є':
            if nah== 'є':
                nah3='наголошений'
            else:
                nah3='ненаголошений'
            print ('[й]- приголосний,сонорний,твердий.')
            print ('[е]- голосний,' + nah3)
        elif col4=='ж':
            print ('[ж]- приголосний,дзвінкий,твердий.')
        elif col4=='з':
            print ('[з]- приголосний,дзвінкий,твердий.')
        elif col4=='и':
            if nah== 'и':
                nah4='наголошений'
            else:
                nah4='ненаголошений'
            print ('[и]- голосний,' + nah4)
        elif col4=='і':
            if nah== 'і':
                nah5='наголошений'
            else:
                nah5='ненаголошений'
            print ('[і]- голосний,'+ nah5)
        elif col4=='ї':
            if nah== 'ї':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[й]- приголосний,сонорний,.')
            print ('[і]- голосний,' + nah6)
        elif col4=='й':
            print ('[й]- приголосний,сонорний,твердий.')
        elif col4=='к':
            print ('[к]- приголосний,глухий,твердий.')
        elif col4=='л':
            print ('[л]- приголосний,сонорний,твердий.')
        elif col4=='м':
            print ('[м]- приголосний,сонорний,твердий.')
        elif col4=='н':
            print ('[н]- приголосний,сонорний,твердий.')
        elif col4=='о':
            if nah== 'о':
                nah6='наголошений'
            else:
                nah6='ненаголошений'
            print ('[о]- голосний,' + nah6)
        elif col4=='п':
            print ('[п]- приголосний,глухий,тваердий .')
        elif col4=='р':
            print ('[р]- приголосний,сонорний,твердий .')
        elif col4=='с':
            print ('[с]- приголосний,глухий,твердий.')
        elif col4=='т':
            print ('[т]- приголосний,глухий,твердий.')
        elif col4=='у':
            if nah== 'у':
                nah7='наголошений'
            else:
                nah7='ненаголошений'
            print ('[у]- голосний,'+ nah7)
        elif col4=='ф':
            print ('[ф]- приголосний,глухий,твердий.')
        elif col4=='х':
            print ('[х]- приголосний,глухий,твердий.')
        elif col4=='ц':
            print ('[ц]- приголосний,глухий,твердий.')
        elif col4=='ч':
            print ('[ч]- приголосний,глухий,твердий .')
        elif col4=='ш':
            print ('[ш]- приголосний,глухий,твердий')
        elif col4=='щ':
            print ('[щ]- приголосний,глухий,твердий')
        elif col4=='ь':
            print (' ')
        elif col4=='ю':
            if nah== 'ю':
                nah8='наголошений'
            else:
                nah8='ненаголошений'
            print ('[й]- приголосний,сонорний,твердий.')
            print ('[у]- голосний,' + nah8)
        elif col4=='я':
            if nah== 'я':
                nah9='наголошений'
            else:
                nah9='ненаголошений'
            print ('[й]- приголосний,сонорний,твердий.')
            print ('[а]- голосний,' +nah9)
