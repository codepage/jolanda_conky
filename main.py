#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

quotes = [
'Abyste cítili tu teplotu ve vašich silách, ve vašich žilách',
'A chci, abyste viděli, jak sem zkušená!',
'A chci hodně jídla, protože sem cigánka',
'A já cejtím s váma!',
'A jéje, to sem se bála!',
'Ale gádžové ne',
'Ale já né, já sem čistá bytost',
'Ale rozsviťte, dou, Vánoce',
'Ale tady máte vy vaše světlo',
'Ale ze sraček můžete vytáhnout se',
'Ano, já se za to nestydim!',
'Ano mluvte do telefonu!',
'Ano, sem cigánka, sem bílá, moje rodiče byli bílí',
'A odejdeš tam kde žiješ',
'A skutečnost je osud',
'A todleto nikdy nebylo ve vysílání',
'Ať ti žehná bůh!',
'A von hodně trpěl, protože trpěl',
'Byla ste zaražená nebo pán může bejt zaraženej',
'Bylo to hodně zakázaný',
'Čím starší, tím je dokolonější',
'Dneska opět žijeme',
'Dobrý večer',
'Dohlídněte na vaši dceru, ať nedělá takový kopičiny',
'Do toho robota',
'Ha? Jedeme?',
'Halo?',
'Hodně budeš někde',
'Hodně si trpěl a hodně si hladoval',
'Hodně vysoko míříš',
'Chcete volat? Nechcete volat? Volejte, nečekejte!',
'Chci pořádný polívky!',
'Chodila sem s mojí maminkou z vesnicí do vesnicí',
'I ten špatnej člověk na každýho spadne',
'I von panbůh se vám odvěčí',
'Jáj bože můj!',
'Jáj bože můj, hoď tam tu sůl na někoho, tám z okna!',
'Jáj, chudák',
'Já ráda vařím, ano, protože je to na mně vidět',
'Kdo chce a vnívá',
'Kdybych mohla, tak udělám hodně Jolandy ze sebe',
'Lidi, co ste v obyváku nebo na sedačce',
'Máte strach!',
'Moje jméno je Jolanda',
'Moje rodina sou všechny bílí',
'Musej mít hladnou hlavu',
'Musela sem dávat pozor, aby nepřijely benga',
'Můžete položit jenom jednu a odpovím vám jenom tři',
'Nečekejte až vyhasnete',
'Nehraju ze sebe nějaká gádžovka',
'Nejezdim támhle na Moarolku',
'Nejsem, jako bych řekla, gádžika',
'Nejsem namyšlená',
'Nejsem nějakej fanatik',
'Nejsem nějaký médium',
'Nejsem nějaký takový, abyste se báli',
'Nejsem vystudovaná, protože na to sem nikdy neměla',
'Nemám nějaký kaviáry nebo nějaký holubata',
'Nenechte se zmát',
'Nepřepínejte kanela',
'Nespinkejte',
'Neustále ste hodně truhlila',
'Nevzlátejte',
'No děkuju za odpověď',
'No tady sem cigánka Jolanda',
'Od těch dětských, od těch dospělostí',
'Pane bože!',
'Pes je přítel člověka',
'Pozor i chlapi mají svoje dny',
'Pro mě je málo tisíc korun',
'Protože tady vidím boží oko',
'Sem cigánka, zaplať pánbůh!',
'Sem kočová cigánka',
'Sem obyčejná cigánka',
'Spadlo to!',
'Ste všechno vykolejenovaná',
'Tady ty ty zlodějové, co maj ty automaty',
'Tady vidim velký špatný',
'Tak cejtí temnotu',
'Tak dobře, zdraví a rodinný stavy',
'Tak, jáj budoucnost',
'Tak jako Jolanda se jmenuju',
'To je vysloveně magogie todleto',
'To je zlá nemoc todleto',
'To není normární!',
'Tvoje budoucnost, hodně míří vysoko',
'Ukažte svoje světlo',
'Vaše vztahy budou nadále vám dobře kvétat',
'Váš manžel hraje automaty?',
'Váš rod je prokletej',
'Vás velice postihne velká dědičnost',
'Vážím tak, kolik mě unese',
'Ve vašem zájemu',
'Vidím, slyším a poslouchám',
'Všechno se to bouří!',
'V tý rodině vidím velký máte chaus',
'Vy máte dobrý? Nemáte nic?',
'Zamíchám na vás váš osud',
'Za totalitě bylo to zakázaný',
'Žijeme z huby do huby',
]

s = random.choice(quotes)
s += '' if s[-1] in '.!?' else '.'
print(s + ' ~Jolanda')
