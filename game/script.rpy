﻿# У цьому файлі міститься скрипт гри.

# Оголошення персонажів, які використовуються в цій грі. Колірний аргумент розфарбовує
# ім’я персонажа.

define St = Character("Стефан")
define Iv = Character("Ів")
define Of = Character("Офіціант")


default cringe_points = 0
default luck_points = 0
default drunk_points = 0

label start:
    jump intro


label change_cringe_points(value):
    $ cringe_points = cringe_points + value
    if cringe_points >= 10 :
        $ renpy.set_return_stack([])
        jump the_end_cringe
        with fade
    else:
        return

label change_luck_points(value):
    $ luck_points = luck_points + value
    return


label change_drunk_points(value):
    $ drunk_points = drunk_points + value
    return


label drink_menu:
    menu:
        "Пиво":
            call change_drunk_points(+5) from _call_change_drunk_points
        "Шампанське":
            call change_drunk_points(+5) from _call_change_drunk_points_1
        "Мартіні":
            call change_drunk_points(+10) from _call_change_drunk_points_2
        "Коньяк":
            call change_drunk_points(+10) from _call_change_drunk_points_3
        "Чай":
            pass
    return



label intro:
    play music "a-jazz-piano-110481.mp3"

    scene bg slide_game:
        fit "cover"
        xoffset 0
        xalign 0
        linear 50:
            xoffset 1.0
            xalign 1.0

    "Ох, щось я трохи хвилююсь."
    "Так, потрібно терміново опанувати себе!"
    "Добре-добре. Фу-у-ух, видихаєм…"
    
    "Що ж вдягти? Це? Чи це? Чи може це?"
    "Поголитись? Гм…"
    scene bg message
    with dissolve
    "Викликати таксі, чи доїхати на метро?"
    "Чи варто подзвонити перед виходом?"
    "Щось я хвилююсь… Я ж вже це казав, вірно?"
    "Ой, а котра година?"
    "Все, пора виходити."
    "Чекаю на нашу зустріч понад усе."


    jump chapter1


label chapter1:

    scene bg entrance day
    play music "sebuah-kenangan-225732.mp3"

    St "Який сьогодні гарний день. Не для вампірів, але я впевнений, Іву буде приємно прогулятись по вулиці."
    "Сонце в зеніті і ти пришвидшуєш крок, ховаючись від нього під просторою парасолею."
    "Ти повільно підходиш до невеликого і дуже затишного ресторану, у якому через кілька хвилин повинна початись приємна зустріч."
    "Людей всередині майже нема, але це і не дивно: робочий день ще не закінчився, та і район насправді не дуже популярний."
    "Серед людей, звісно."


    scene bg rest day


    "Ти заходиш всередину ресторану і сідаєш за столик подалі від дверей, барної стійки та приміщення для персоналу."
    St "Сподіваюсь, йому теж тут сподобається."
    St "Що ж, скоро побачимо."
    "Ти даєш зрозуміти офіціанту, що ще чекаєш на свого супутника і щохвилини дивишся на екран телефона, сподіваючись пришвидшити час."
    "На жаль чи на щастя, без спеціалізованих знань зробити це майже неможливо."
    "…"
    "Час потроху спливає і ти починаєш трохи нервуватись."
    "Ів попереджав, що може трохи затриматись на роботі, і ти заспокоюєш себе думкою, що саме так і сталося."
    "Він просто затримується на десять хвилин, Стефане."
    "Просто набридливий клієнт ніяк не покладе слухавку і не відпустить його по своїм справам."
    "Це ще навіть не запізнення, якщо так подумати."
    "…"
    "Він же не міг забути?"
    "Чи ще гірше - свідомо не прийти?"

    Iv "Як сталось, що такий гарний упирчик сидить в цьому кафе один і зовсім без охорони?"
    show st 5_2
    Iv "Не боїшся, що вкрадуть?"
    St "І тобі привіт."
    Iv "Все добре?"
    St "Просто я не очікував від тебе такого привітання."
    Iv "Так як я трохи запізнився, то вирішив діяти несподівано, щоб ти на мене не бурчав."
    St "Нічого страшного. У тебе щось сталось?"
    show st 5_1
    Iv "Мене зупинила поліція і допитувала протягом години. "
    St "Жах! Чому саме тебе?"
    show st 11_1
    Iv "Вони шукають найкрасивішого мужчину в усьому Парижі, але ти можеш бути спокійним: я тебе не видав."
    St "…"
    show st 3
    Iv "Я знав, що ти оціниш."
    show st 9
    St "Хіба на трієчку з п’яти. Заснув на книжці з жахливими фразами для знайомств?"
    Iv "Скоріше за роботою."
    St "Її настільки багато?"
    show st 7
    Iv "Ох."
    show st 10_2
    Iv "Знаєш, я колись дивився документальний фільм про адронний колайдер. І у ньому працівник скаржився на те, що «полагодили одне - зламалось інше. Полагодили інше - потекла якась труба. Полагодили трубу - посипалась стіна». І так до безкінечності."
    Iv "У мене зараз настрій приблизно як у того мужика."
    St "Маю надію, що до кінця вечора мені вдасться його покращити."
    show st 18
    Iv "Побачимо."
    Iv "Бо вже нема сил."
    Iv "Іве, подзвони йому! Іве, він чекає на правки! Іве, а де файл?"
    show st 10_1
    Iv "А Ів навіть кави не встиг випити."
    St "Моя ж ти бідося."
    show st 4_1
    St "Чи можу я тебе якось розрадити?"

    menu:
        "Ти голодний?":
            pass

    show st 8
    Iv "Так, я б зараз цілого кабана з’їв, якщо чесно."
    St "Наскільки я пам’ятаю, у них смачні стейки."
    show st 14
    Iv "Стейки, кажеш?"

    call change_cringe_points(+1) from _call_change_cringe_points


    show st 9
    Iv "От його і візьму."
    St "Алкоголь?"
    Iv "Ну…"

    $ choosen_drink = ""

    menu: 
        "Так":
            show st 7
            Iv "Ой, так, хочу. Бо це був якийсь день відчинених дверей в дурдомі."
            St "Замов собі…"
            call drink_menu from _call_drink_menu
            show st 8
            Iv "Мені подобається. Саме те, що зараз потрібно."

        "Ні":
            pass

    "Офіціант швидко записує ваше замовлення і знову залишає вас наодинці."
    show st 10_1
    Iv "Уф… Мабуть, варто закінчити з цим замовником і піти у невелику відпустку."
    St "І як ти будеш відпочивати?"
    St "Будеш весь час читати книги і гуляти, чи кудись поїдеш?"
    show st 11_1
    Iv "Це залежить не лише від мене."
    St "В якому сенсі?"
    show st 12_22
    Iv "Якщо один підстаркуватий упирчик зацікавиться спільним відпочинком, тоді, скоріш за все, я кудись поїду."
    St "…"
    St "Можливо, він зацікавиться."
    show st 6
    Iv "Я так і подумав."
    St "І куди ти хочеш з’їздити?"
    show st 4_1
    Iv "Куди?.."
    Iv "Було б гарно побувати десь у горах. Десь, де тихо, ліс, одинока хатинка, озеро і навколо зовсім нікого, крім нас."


    menu:
        "Мені подобається":
            call change_luck_points(+5) from _call_change_luck_points
        "Це не мій тип відпочинку":
            call change_luck_points(-5) from _call_change_luck_points_1
            show st 16
            Iv "Шкода. Я люблю такий відпочинок на природі."
            Iv "Ну… Розумієш… Там так гарно і тихо."
            Iv "І… і вовку завжди є де побігати..."
            Iv "Він… Я люблю таке усамітнене і затишне… хм… лігво."

    show st 8
    Iv "А ще можна побувати десь на морі чи океані!"
    Iv "Уяви: усамітнений пляж. Ми сидимо на піщаному березі під зонтиком, і хвилі безкінечно накочуються і відступають."
    Iv "І чайки в небі голосно кричать."
    Iv "І пахне сіллю. І морозивом, яке у мене в руках."
    show st 7
    Iv "Чому ти з мене смієшся?!"
    St "Це дуже мило."
    show st 5_2
    Iv "А ти на спеці випадково не розтанеш, як у тих стрьомних історіях про вампірів?"
    show st 5_1
    St "Хіба у твоїх обіймах."
    Iv "…"
    show st 2
    Iv "Це навряд. Якщо я вже за щось чи за когось схопився, то від мене просто так не вислизнеш."
    St "Обов’язково перевірю."
    Iv "А ти де любиш відпочивати?"
    show st 9
    St "Мені теж імпонує бути десь, де тихо і немає людей."
    St "Найчастіше я знаходжу якесь непопулярне місце за допомогою Інтернету і їду туди."
    Iv "Я думаю, всі ці місця не просто так непопулярні."
    St "Ну… Не завжди. Можу знайти тобі фото останнього відпочинку, якщо даси кілька хвилин."
    show st 13
    Iv "Ой, ну ні! Ніяких телефонів, поки ми тут."
    St "Добре-добре, я просто спитав."
    show st 8
    Iv "І де ти був?"
    St "Часто якісь кряжі, гірські дороги, забуті розвалини. І…"
    show st 3
    St "…"
    Iv "Що?"
    St "Можеш не стримувати себе."
    show st 5_1
    Iv "…"
    St "І печери."
    show st 5_2
    Iv "…"
    Iv "…"
    Iv "Я аж не знаю, з якого жарту почати."
    St "Та вже вибери якийсь."
    Iv "Потягнуло до родичів?"
    show st 6
    St "Хто знає. Природа вампірів до кінця ще не вивчена."
    St "Але якщо серйозно, то під час першої нашої поїздки у нетуристичну печеру ми заблукали і натрапили на купу кажанів, які спали під стелею."
    Iv "Ого! А ти можеш з ними спілкуватись? Ну, розумієш їх?"
    show st 5_1
    St "Отак тобі всі таємниці і розкажи на першому побаченні."
    Iv "Цікаво же."
    St "Відповім так: нам вдалось розбудити ту колонію і вона допомогла нам вибратись з печери."
    Iv "Вау! Тобто, це не казочки? Ти їм наказав провести вас до виходу?"
    St "Хм… Може і наказав, але обгидили нас вони явно з власної волі."
    show st 3
    Iv "Кажуть, то до грошей."
    St "До грошей то голуби. А це до великого прання."
    show st 9
    Iv "До речі, ти сказав «ми». Ти там був з друзями?"
    St "Ні."

    show st 10_33
    Iv "А з ким?"
    St "З хлопцем. Колишнім."
    show st 10_2
    


    Iv "Теж любив ходити там, де нога нормального нелюда не ступала?"
    St "Не дуже, але на кілька годин кудись вирватись був не проти."
    Iv "Я б теж не дуже хотів блукати невідомими печерами, якщо чесно."
    St "Так я ж і не тягну тебе."


    menu:
        "Поки що":
            call change_luck_points(+5) from _call_change_luck_points_2
        "Промовчати":
            call change_luck_points(-5) from _call_change_luck_points_3

    show st 1_1
    Iv "О, а ось і наше замовлення!"
    # Показати перехід через ds
    "Кілька хвилин ви сидите мовчки, вгамовуючи перший голод."
    show st 8
    Iv "Ох!"
    Iv "Смачно."
    Iv "Навіть настрій покращився."
    St "Я радий. Це було неважко."
    Iv "А як ти зазвичай справляєшся з поганим настроєм?"
    Iv "Типу, чи є у тебе якісь особисті прийоми?"
    St "Дай подумати."
    show st 4_2
    Iv "Даю."
    St "Я насправді рідко маю кепський настрій. А от що допомагає…"
    St "Хм…"
    show st 9
    St "Точно рятує спілкування з близькою людиною. Кілька хвилин - і я забуваю, через що сумував."
    St "Ще можу відволіктись на щось, приготувати вечерю для когось чи подивитись якийсь цікавий ролик в інтернеті."
    show st 11_1
    Iv "Тобто відправлена у правильний момент хтивка виконає відразу дві задачі і підніме ще й настрій?"
    Iv "Запам’ятаю."
    St "…"
    St "Головне, щоб настрій підіймався тільки у мене, а не у людей поруч."
    Iv "Ну, це вже будуть не мої проблеми."
    show st 12_22
    Iv "Це ти соромишся, що хтось побачить такі фото, чи ревнуєш?"

    menu:
        "Соромлюсь":
            call change_cringe_points(+2) from _call_change_cringe_points_1 
        "Ревную":
            pass

    show st 5_1
    Iv "…"
    Iv "Ти такий милий."
    Iv "Ти завжди такий милий?"
    St "…"
    show st 5_2
    # Ілюстрація Ів сильно усміхається
    St "…"
    St "Тільки коли сплю зубами до стіни і не кусаюсь."
    Iv "І в яких випадках ти найчастіше кусаєшся?"
    St "Все тобі потрібно знати."
    show st 5_1
    Iv "Ну я ж перевертень, я люблю все… винюхувати."
    show st 11_1
    Iv "То коли?"

    menu:
        "Тільки коли мені хтось дуже подобається":
            call change_cringe_points(+2) from _call_change_cringe_points_2
            Iv "І коли мені пора починати переживати?"
            St "В сенсі?"
            show st 13
            Iv "Ми сидимо в цьому ресторані вже сто років, а я досі некусаний."
            St "Я… Не при всіх же."
            show st 11_1
            Iv "А як же всі ті упущені можливості, коли ми годинами ходили тими тихими темними вуличками Парижа?"
            Iv "То ж святе, хапай і кусай!"
            St "Я ж не маніяк якийсь."
            show st 11_1
            Iv "Шкода."

        "Коли хтось дуже довго пробиває товар на касі супермаркета":
            show st 3
            Iv "А-ха-ха-ха! Я б тебе після першого ж разу не пускав у магазин."
            Iv "Або виділив би окрему касу. Для найнетерплячіших."
            St "Нас і так багато хто відділяє від основної маси."
            show st 6
            Iv "Воно і не дивно, якщо тебе кусають за дупу, поки ти зважуєш собі моркву на обід."

    show st 7
    Iv "Гей, ти чого?"
    Iv "Я ж пожартував."
    St "Пробач. Раптом згадались всі спроби суспільства якимось чином від мене відгородитись і стало сумно."
    Iv "Я щось не подумав."
    show st 4_1
    Iv "…"
    show st 5_1
    Iv "То з мене хтивка?"

    show st 9
    Of "Бажаєте ще щось?"


    "Офіціант, здається, з’являється біля вас нізвідки."
    "Ів здригається від несподіванки, але до твого здивування утримується від незадоволеного тону."
    show st 14
    Iv "Я, мабуть, візьму ще…"

    call drink_menu from _call_drink_menu_1

    show st 9
    St "Мені теж ще один келих, будь ласка."
    "Офіціант записує ваше замовлення і за кілька хвилин приносить його."
    show st 16
    "Кілька хвилин ви сидите мовчки, думаючи про щось своє."
    Iv "…"
    Iv "Хм."
    show st 4_1
    Iv "Стефане, я можу спитати?"
    St "М-м-м?"
    St "Що саме?"
    show st 8
    Iv "Наскільки…"
    Iv "Тебе сильно обтяжує бути вампіром?"

    menu:
        "Сильно":
            call change_luck_points(-5) from _call_change_luck_points_4
        "Не дуже":
            call change_luck_points(+5) from _call_change_luck_points_5

    show st 9
    St "Я приблизно чогось такого і очікував правду кажучи."
    St "Тому скажу так: є свої недоліки, але жити можна."
    St "До упередженого ставлення з часом звикаєш і майже не звертаєш на нього увагу."
    show st 8
    St "Поки не прилетить. В усіх сенсах."
    St "Важче було звикнути до нового… хм, раціону…"
    St "Якийсь час все ще хотілось купити і з’їсти улюблені продукти, але за тиждень-два зникло і це бажання."
    St "Ще довелось звикати до відсутності запрошувачів у деяких магазинах."
    show st 9
    St "Іноді забував, що краще не виходити на сонце, але і це дрібниці. Почав більше гуляти ввечері та і все."
    St "Мабуть, найгірше з усіх наслідків це постійно холодне тіло, але то вже не моя проблема."
    St "Тому ні, мене не сильно обтяжує бути вампіром."
    show st 2
    Iv "Ти так легко погоджуєшся з обмеженнями."
    Iv "Сказав би хтось мені, що не можна бігати по сонцю! Відразу ж хочеться вийти кудись на пляж і розлягтись зірочкою на піску."
    show st 1_2
    Iv "Чого ти смієшся? У мене аж руки зачухались прямо зараз так і зробити."
    St "Не знав, що ти такий бунтар."
    show st 2
    Iv "Мені у дитинстві, а особливо протягом підліткового віку, взагалі неможливо було щось заборонити."
    show st 10_2
    Iv "Тобто, ну, можна було, але я з тим був категорично незгоден!"
    St "Бідні твої батьки."
    Iv "Як сказати."
    Iv "Я, хоч і протестував, але слухався."
    show st 4_2
    St "Здається, зараз майже нічого не змінилось."
    St "…"
    show st 11_1

    Iv "Тобто?"
    St "…"
    St "…"
    Iv "Та кажи вже."

    menu:
        "Ти досі іноді слухаєшся старших?":
            call change_cringe_points(+2) from _call_change_cringe_points_3
            call change_luck_points(+5) from _call_change_luck_points_6

    pause
    show st 12_22
    Iv "…"
    Iv "Хочеш перевірити?"
    Iv "Для тебе, мій любий упирчику, я готовий бути і слухняним хлопчиком, і розпусним розбишакою."
    Iv "І це все за одну ніч."
    St "Кхм…"
    St "Щось я… хм…"
    show st 11_1
    Iv "Я вже казав, що ти дуже милий, коли соромишся?"
    St "Сто разів."
    show st 5_1
    Iv "Отже."
    Iv "Ти любиш ігри?"
    St "Що?"
    show st 5_2
    St "Ігри?"
    St "Трохи неочікуване питання, якщо чесно."
    St "Гм…"
    St "Ти про про які ігри питаєш? Комп’ютерні? Чи настільні?"
    show st 5_1
    Iv "Настільні."
    St "Ой, дивлячись які."
    St "Кілька разів пробував грати, було навіть цікаво. Згадати б назву…"
    St "Головне щоб процес не затягувався надовго."
    show st 11_1
    St "…"
    Iv "…"
    St "Чого ти?"
    Iv "Я теж люблю настільні ігри."
    show st 12_22
    Iv "Зіграємо?"
    St "О боги…"
    Iv "Розкладеш мене прямо тут на столі?"
    St "…"
    St "Іве…"
    St "Ти на якісь дурнуваті курси зваблення записався?"
    show st 4_2
    Iv "Ображаєш! Писав дещо по роботі, от і увібрав у себе нові корисні знання."
    Iv "Працює ж."
    Iv "А чого не любиш довго затягувати? Здоров’я вже не те?"
    show scene3
    show st 5_1
    St "Звісно, мені ж вже не вісімнадцять років. І пальці на погоду крутить, і щелепа при позіханні хрускає, і важкувато на п’ятий поверх пішки підійматись."
    St "Та і ціни на тих лікарів зараз такі, що треба себе берегти, бо ніякої зарплатні на них не вистачить. І страховок."
    show st 4_1
    hide scene3
    show scene2
    Iv "Ой, не кажи."
    Iv "Я місяць тому прийшов до стоматолога спиляти ікло, бо щось дряпатись почало при перекиданні у вовка, а він як заглянув в мої глибини…"
    show st 14
    Iv "Може і самому цойгокнутись у вампіра, дешевше буде."
    show st 10_2
    Iv "Треба було зуби лікувати, поки батьки забезпечували, чесне слово."
    St "Знайомо. Але вже не актуально."
    Iv "Добре тобі!"
    St "Не жаліюсь."
    Iv "Нічого, буде колись і на тебе кара божа."
    St "Та, здається, її вже наслали."
    hide scene2
    show st 11_1
    Iv "Пф. Це ти мене ще на повню не бачив. От тоді згоден, тоді гайки всім навколо."
    St "…"
    Iv "Не подобається?"
    St "Навпаки."
    show st 12_22
    Iv "Тобто ти не тільки любиш гратись, а ще й трохи мазохіст."
    Iv "Так і запишемо."
    St "До речі, про повню. Розкажи, як це відбувається у перевертнів."
    show st 5_1
    Iv "Що саме тебе цікавить?"
    St "Ти казав, що у вас є спеціальні місця, де можна побути вовком. Цікавить, як там все влаштовано."
    show st 7
    Iv "Ой, та насправді нічого такого."
    Iv "Кілька великих приміщень, де можна побігати, поспати, подряпати стіну, повити."
    Iv "Посоціалізуватись з іншими відвідувачами."
    Iv "Всередині все зроблено під ліс з галявинами, але як на мене це суцільний несмак."
    Iv "І синтетикою смердить. Ці пластикові голки на ялинках колись доведуть мене до сказу."
    show st 4_1
    Iv "Але то для таких невибагливих, як я. Є простори дорожчі, там тобі і осіннє листя розкидають, щоб на ньому повалятись, і води свіжої в джерело наллють."
    Iv "Якщо є бажання, тебе можуть погодувати чимось, що ти сам принесеш, або обереш з меню."
    St "А якщо це… хм… сезон спарювання?"
    show st 2
    Iv "Тоді або сиди вдома, або кімнати розділяють по статям та і все."
    show st 1_2
    Iv "Хоча це відчувається як якесь знущання насправді. Ніби тебе десь блоха кусає, а ти не можеш її вичесати з себе."
    St "А… хм…"
    show st 5_2
    Iv "Відчуваю якесь сороміцьке питання."
    St "Воно, мабуть, не зовсім коректне і занадто особисте."
    show st 5_1
    Iv "А от тепер стало ДУЖЕ цікаво. Питай, тобі можна."

    menu:
        "Тебе ж потрібно навпаки, ізолювати від чоловічої статі в такі періоди":
            call change_cringe_points(+2) from _call_change_cringe_points_4
            call change_luck_points(+5) from _call_change_luck_points_7
            Iv "Ой, в такі моменти мені в мені скоріше прокидається бажання гризтись з усіма в тій кімнаті."
            Iv "Іноді так і стається. Але не з моєї ініціативи."

        "Та ні, залишу це питання на майбутнє":
            call change_luck_points(-5) from _call_change_luck_points_8
            show st 16
            Iv "Шкода, але тиснути не буду."
            Iv "Поки що."
    
    show st 10_2
    Iv "Ох, не люблю повню."
    Iv "Тобі і так погано, а ще треба кудись діти всю накопичену енергію. Бігаєш як дурний півтора дні, а потім відсипаєшся ще добу."
    Iv "І нікому ж не поясниш на роботі, що у тебе все життя згідно місячного календаря рухається, дедлайни ж не чекають."
    St "А можна якось цей період полегшити?"
    show st 10_1
    Iv "Ніяк. Хіба слухати моє скавчання, робити масаж, бо все тіло ломить, годувати курячими суглобами в три ночі."
    St "Я не проти."
    Iv "…"
    show st 11_1
    Iv "Сьогодні ж збираю речі."
    St "І багато їх у тебе?"
    St "Замовити вантажівку, чи і тачанкою обійдемось?"
    Iv "Не дуже і багато."
    Iv "Так, дві шафи з одягом, трохи творчого мотлоху, картини, книги, велосипед, кухонне приладдя, трохи непрацюючої техніки, яку треба віднести полагодити, сестрині штуки, які батьки не повинні ніколи побачити, трохи меблів, речі для моєї другої форми, три матраци, кілька штук для ванни…"
    Iv "Ну добре, не кілька, багато."
    Iv "В багажник має поміститись."
    St "Здається, нам треба буде зняти не квартиру, а цілий котедж."
    show st 3
    Iv "Було б гарно, але я вже підпиляв ікло, тож найближчі півроку я живу в коробці біля батьківської хати."
    window hide

    play sound "<from 0 to 4>vibration.mp3" volume 55
    pause

    show st 20
    Iv "Ой, ну кому я вже потрібен?"
    Iv "Замовник. Цікаво, правки по тексту, чи спитає мій банківський рахунок?"

    menu:
        "Замовник може трохи почекати":
            call change_luck_points(+5) from _call_change_luck_points_9
        "Відповідай, це може бути терміново":
            jump the_end_2
    

    show st 8
    Iv "Маєш рацію. Нехай трохи почекає, і так весь день мозок виносив."
    Iv "…"
    St "Не згадуй роботу, вона зараз тут ні до чого."
    Iv "Мені важко перемикатись. Особливо коли був отакий день як сьогодні."
    St "До цього моменту тобі все вдавалось."
    show st 4_2
    Iv "Іноді я непоганий актор."
    St "Головне, щоб це не було на постійній основі."
    Iv "Не на постійній. Так, епізодично. Коли маю настрій."
    show st 12_22
    Iv "Можу побути твоїм песиком."
    Iv "А можу і хазяїном песика."
    Iv "Як тобі більше подобається? Любиш песиків?"
    St "А раптом я не по песикам?"
    show st 11_1
    Iv "Отакої. Мене ще ніхто не кликав на побачення і не заявляв на ньому, що він не по песикам."
    Iv "Не по мужчинам - кожен третій так точно."
    show st 10_1
    Iv "Ні-ні, Іве, я не такий, я у мене взагалі дружина і двоє дітей, ага."
    Iv "Ой, вибач."
    Iv "Згадалась пара чортяк."
    St "Та нічого. І добре, що вони виявились такими чортяками, бо ми б зараз тут не сиділи."
    show st 8
    Iv "Твоя правда."
    St "Люблю песиків. Чесно."
    show st 6
    Iv "І шерсть за ними теж любиш прибирати?"
    St "І шерсть за ними обожнюю прибирати. І кігті стригти. І лапи мити. І слухати їх виття в три ночі."
    Iv "Дивлюсь на твоє багряне обличчя і не вірю, що у тебе низька температура тіла."
    Iv "Ти зараз згориш прямо посеред кафе."
    show st 5_2
    Iv "Давай я тебе доб’ю: можливо, я носій генів не тільки перевертня, а й медузи горгони."
    St "…"
    St "О боги…"
    show st 5_1
    Iv "Бо при погляді на мене у тебе таки щось скам’яніє."
    St "..."
    St "Рятуйте."
    Iv "Я ще й не починав."
    Iv "Але можу припинити."
    show st 12_22
    Iv "Як забажаєш, мій упирчику."

    menu:
        "Мені все подобається":
            call change_luck_points(+5) from _call_change_luck_points_10
        "Мені трохи… незручно":
            call change_luck_points(-5) from _call_change_luck_points_11

    Iv "Хех."
    Iv "Знаєш, до нашого знайомства я кілька разів звертав на тебе увагу в барі."
    St "Це було взаємно. Але тепер мені цікаво, якою була причина такого підвищеного інтересу до звичайного відвідувача."
    show st 17
    Iv "Ну…"
    Iv "Не важливо."
    Iv "Але мені завжди здавалось, що ти дуже самовпевнений і засоромити тебе - майже неможлива задача."
    St "Дивлячись коли."
    Iv "…"
    show st 5_2
    Iv "Упирчику, ти не уявляєш, як мені цікаво перевірити ВСІ варіанти."
    St "Можливо, тобі навіть вдасться. Колись."
    Iv "Я дуже терплячий."
    St "Я б так не сказав."
    show st 5_1
    Iv "Я знаю тебе довше ста годин, а досі не бачив тебе оголеним."
    Iv "Я. Дуже. Терплячий."
    St "Та не обманюй, я тобі висилав фото."
    show st 11_1
    Iv "Оте сонне біля дзеркала із зубною щіткою в роті?"
    Iv "Воно було миле, але навіть до рейтингу 16+ не дотягує."
    St "Я взагалі стараюсь не робити такий контент, якщо чесно."
    show st 6
    Iv "Оу."
    Iv "Чому?"
    St "Мені б не хотілось, щоб ці фото чи відео з’явились десь у мережі. Чи у роботодавця. Чи друзів."
    St "Та і на що там, правду кажучи, дивитись."
    St "Приходь в гості і дивись собі, а не оце все."
    Iv "…"
    show st 5_1
    Iv "У-у, це запрошення?"
    St "…"
    St "Якщо будеш себе гарно вести - покличу до себе на каву."
    show st 12_22
    Iv "Я хороший песик. Чесно-чесно. Особливо якщо мене файно попросити."
    St "Вірю. Весь ресторан тобі вірить."
    Iv "Весь ресторан хай не підслуховує. І не підглядає."
    Iv "Гм…"
    Iv "Це якщо саме я запрошу тебе до себе додому, то це Я повинен буду тобі щось показати?"

    menu:
        "Не обов’язково":
            show st 9
            call change_luck_points(-5) from _call_change_luck_points_12
            Iv "Мене вчили, що гостям дають найкраще."
            St "Якщо усіх так… гарно приймати, то ніяких… ресурсів не вистачить."
            Iv "Так і я не дуже гостинний."

        "Я б глянув, звідки у тебе хвіст росте":
            call change_luck_points(+5) from _call_change_luck_points_13
            call change_cringe_points(+2) from _call_change_cringe_points_5
            show st 11_1
            Iv "Давай вийдемо у вбиральню, покажу."
            St "Та мені ж не шістнадцять років, щоб бігати у вбиральні за хлопцями і дивитись на їх… хвости."

    show st 8
    Iv "…"
    Iv "Що?"
    St "Маю так багато питань, але не впевнений, що хочу отримати на них відповіді прямо зараз."
    show st 9
    Iv "Тоді я відволічу тебе. Любиш приймати гостей вдома?"
    St "Гостей?"
    St "Дивлячись кого. Найбільше люблю влаштовувати посиденьки з найближчими друзями, але це вдається досить рідко."
    St "Сам розумієш, то у мене робота, то у них нирка заболіла, то племінники народжуються, то ще якась історія. Важко зібратись всім разом."
    show st 8
    Iv "А найменше?"
    show st 3
    St "Троюрідну тітку двоюрідної сестри мами, яку батькам обов’язково треба привезти з собою щоб показати, як я облаштувався."
    St "Добре, що їм теж важко зібратись разом."
    St "А ти?"
    show st 2
    Iv "Я не дуже люблю гостей, адже совість каже, що перед цим дійством треба поприбирати вдома, а мені зазвичай лінь цим займатись."
    show st 4_1
    Iv "Не подумай, там не гори сміття, але змахнути пилюку з поверхонь точно доведеться."
    Iv "Краще ходити в гості. Прийшов, посидів, соціалізувався, обмінявся останніми новинами, поїв, випив, пішов додому."
    show st 1_1
    Iv "Краса ж!"
    St "Якщо прийду я, то можеш не прибирати. Я не буду роздивлятись пилюку на твоїх поличках."
    show st 5_1
    Iv "Будемо її створювати, вибиваючи з матрацу на ліжку?"
    Iv "Чи навпаки, витремо власними тілами?"
    show st 5_2
    Iv "Чи виконаємо мою мрію і організуємо мені регулярний клінінг?"
    St "…"
    St "Краще йти в гості до мене."
    show st 12_22
    Iv "Але я ж ще той… песик. Один раз запросиш - ризикуєш більше не вигнати."
    Iv "Принаймні поки добряче не висплюсь."
    St "З цим проблем не має виникнути. Принаймні, ніхто не скаржився."
    Iv "А на мене - дуже навіть скаржились."
    St "Чому?"
    show st 3
    Iv "То похропую трошки, то посилаю замовника уві сні, то кручусь, то сіпаюсь."
    St "Які ніжні."
    Iv "От я теж так думаю."
    show st 17
    Iv "Хоча здавалось, що після моєї піжами з… хм… після моєї піжами не було чому дивуватись."
    St "Піжами з чим?"
    show st 3
    Iv "Колись покажу. То треба бачити."
    Iv "Сестра подарувала із коментарем «щоб любов примножувалась», але щось як я її вдягаю, то любов якось викликає таксі і більше не вертається."
    St "Значить, то така любов."
    show st 6
    Iv "Еге ж. До етапу зачарованих на любов трусів досі ніхто не дійшов."

    menu:
        "Мабуть, то на краще":
            call change_luck_points(-5) from _call_change_luck_points_14
            Iv "Навіть не знаю. Мені хотілось хоч раз їх комусь показати."
            Iv "Хоча… А ні, забудь."
        "Ніколи не бачив панталонну магію":
            call change_luck_points(+5) from _call_change_luck_points_15
            Iv "Це дуже легко виправити."

    show st 5_1
    St "…"
    St "Що таке? У мене кров на вусах лишилась?"
    Iv "…"
    Iv "Ти такий милий."
    St "Здається, хтось вже п’яненький."
    show st 5_2
    Iv "Пф, від чого? Не сміши."
    Iv "От від Клода я можу вийти трохи під градусом, але зараз ні в одному оці."
    Iv "…"
    Iv "Ти любиш адреналін?"
    St "Гм… Залежить від способу його отримання."
    St "Щось небезпечне для життя я не роблю, але залізти на якусь багатоповерхівку - це цікаво."
    show st 5_1
    Iv "Каже упирчик, який принципово не виходить в двері, а стрибає у вікна."
    St "Це абсолютно безпечно."
    St "Ну, для мене так точно."
    St "А що?"
    show st 5_2
    Iv "…"
    Iv "Ти такий цікавий горішок."
    Iv "Іноді мені здається, що я тебе розкусив, зрозумів, що у тебе всередині, а потім виявляється, що нічого подібного."
    Iv "Так цікаво."
    Iv "Цікаво намацувати твої кордони. В усьому."
    St "Це взаємно."
    St "Близьким людям я дозволяю… дуже багато."
    show st 11_1
    Iv "…"
    St "…"
    St "Давай, бо я ж бачу, як воно тебе мучить."
    show st 12_22
    Iv "…"
    St "Хочеш промацувати не тільки емоційні кордони?"
    Iv "Ще раз повторю: ти такий милий."
    Iv "Проте так, ти все вірно підмітив."

    window hide
    pause
    

    St "Це що, твоя нога під столом?"
    show st 5_2
    Iv "Так. А має бути рука?"
    menu:
        "Я б не відмовився":
            call change_luck_points(+5) from _call_change_luck_points_16
            call change_cringe_points(+2) from _call_change_cringe_points_6
        "Востаннє я щось таке робив років у шістнадцять":
            call change_luck_points(-5) from _call_change_luck_points_17
    
    show st 5_1
    Iv "Не хвилюйся, я не зроблю нічого протизаконного."
    Iv "Чи ти хотів би?"
    St "Можливо."
    Iv "Але ми не будемо?"
    St "Не сьогодні."
    show st 11_1
    "Нога Іва дуже обережно торкається твоєї щиколотки, акуратно погладжуючи її кінчиками пальців."
    "Ти намагаєшся зосередитись на його словах, але тобі це погано вдається."
    Iv "Не напружуйся ти так."
    Iv "Дихай."
    "Ти швидко перевіряєш, чи не дивиться хтось у вашу сторону, але і персонал, і відвідувачі зайняті власними справами та розмовами."
    Iv "Чи може ти не любиш усілякі тактильні штуки, м?"

    menu:
        "Люблю, але не на людях":
            call change_luck_points(-5) from _call_change_luck_points_18
        "Люблю. І приймати, і віддавати":
            call change_luck_points(+5) from _call_change_luck_points_19


    show st 4_2
    Iv "Не хвилюйся."
    Iv "Я так, дражнюсь трошки."
    St "Та я і не хвилююсь. Просто спостерігаю."
    Iv "І як?"
    St "Цікаво."
    show st 6
    Iv "В цьому і є головний сенс подібних зустрічей, чи не так?"
    show st 17
    "Ів продовжує погладжувати твою ногу, проте встановлені власною совістю рамки не перетинає."
    "По твоєму тілу мимоволі пробігають приємні мурахи."

    scene bg rest night
    show scene1
    show st 10_33
    Iv "Оу. Час з тобою завжди летить так непомітно."
    St "Я теж здивований, що вже так пізно."
    St "Хочеш ще чогось? Кави, наприклад?"
    Iv "Ні, дякую. Я ситий, напитий і наговорений."
    Iv "Наступного разу я ж обираю місце зустрічі?"
    St "Так."
    show st 8
    Iv "Тоді покажу тобі, де я раніше любив проводити час годинами."
    St "Чому «любив»?"
    Iv "Переїхав."
    St "Зрозумів. Добре, мені вже дуже цікаво, де це."
    Iv "Багато не…"

    play music "<from 0 to 58>horse.mp3" volume 0.5

    show st 18
    Iv "Дідько, а що так голосно?"
    Iv "Гр-р-р!"
    Iv "Намагаються вигнати всіх перевертнів чи що?"
    St "Не зрозумів."
    show st 19
    Iv "Вуха чутливі до звуків навіть у людській формі."
    Iv "Я і так чую, як на кухні дехто після нарізки салату руки не помив і взявся ними на за м’ясо, а цей концерт взагалі мене вбиває."
    St "Підемо звідси?"
    Iv "Так, пора йти. І так довго просиділи, пора іти відсипатись перед новим робочим днем."
    St "А у мене завтра вихідний."
    Iv "Радий за тебе, але не від щирого серця."
    "До вас підходить офіціант і ви просите його принести розділений рахунок."
    show st 20_3

    Iv "Мені сьогодні як раз мали заплатити за останній проєкт, тож гуляєм на всі."
    Iv "Тільки трошки на метро лишити треба."

    menu:
        "Оплатити свою частину чеку":
            pass

    play sound "<from 0 to 2>payment yes.mp3" volume 5
    St "Метро спільними зусиллями ми точно подолаємо."
    play sound "<from 1 to 2>mono.mp3" volume 3
    St "Можеш не хвилюватись."
    show st 20_1
    Iv "Не буду."
    Iv "Тепер я."
    pause
    window hide
    play sound "credit_rh2yfreesound_pic.mp3"
    play sound "payment_error.mp3" volume 2
    show st 20_2
    Of "Оплата не проходить. Спробуйте ще раз."
    Iv "Ем-м-м… Ну добре."
    St "Якщо що…"
    Iv "Все добре."
    play sound "credit_rh2yfreesound_pic.mp3"
    play sound "payment_error.mp3" volume 2
    show st 20_3
    Iv "От чортівня! Мабуть, замовник таки ще не оплатив проєкт."
    show st 13
    Iv "Нічого, нічого. У мене є готівка."
    Iv "Зараз, кілька секунд."
    show st 21_2
    St "…"
    Iv "Монетки теж гроші!"
    St "Тобі точно не потрібна допомога?"
    show st 21_5
    Iv "Взагалі жодних проблем. Тільки у замовника, якого завтра чекає невеличкий скандал."
    Iv "Нарешті позбавлюсь від цієї дрібноти. Так, скільки там по рахунку?"
    St "Ти зараз схожий на дракона, який сидить на купі золота і нікого до неї не підпускає."
    show st 21_3
    Iv "Ти дивись, а то ще почують і потім десь за рогом популярно нам пояснять, чому подібні стереотипи шкодять їм у реальному житті."
    St "Цікаве вийде закінчення дня."
    show st 21_1
    Iv "У тебе є знайомі травматологи?"
    St "Звісно є, але я б не хотів потрапити до них на прийом. Вчились вони так собі."
    Iv "Тепер і мені треба контакти, щоб точно до них не потрапити."
    show st 21_2
    Iv "Тридцять чотири, тридцять п’ять… А стоп! Чи ні, не стоп… Все заново."
    Iv "Не дивись так на мене!"
    St "Та хоч три години рахуй свої гроші, я нікуди не спішу. І вуха у мене не болять."
    show st 21_5
    Iv "…"
    St "…"
    show st 21_2
    Iv "Десять… Двадцять…"
    Iv "Чому ти так на мене дивишся?"
    St "Просто цікаво, що буде, якщо я зараз повторю твої дії кілька хвилин тому."
    show st 21_3
    Iv "Тоді ми звідси ніколи не вийдемо."
    Iv "Так, не заважай. Або заважай, але через пару хвилин."
    Iv "…"
    show st 21_2
    Iv "П’ятдесят три… Ага…"
    Iv "Тридцять… Сорок… Все! Ну от, жодних проблем!"
    St "Можна подумати, що ти пограбував якогось волоцюгу."
    show st 8
    Iv "О, маю на цю тему прикольну історію! Зараз розповім…"
    Iv "Йдемо?"

    menu:
        "Так":
            pass

    if luck_points >= 10:
        jump the_end_3
    else:
        jump the_end_4










label the_end_cringe:
    play music "kek.mp3"
    show iv 1
    Iv "Га? Що сталось?"
    Iv "Стефане?"
    St "Цеє... Здається я десь загубив свою льотну ліцензію і тепер повинен прилітати додому до сьомої вечора."
    Iv "Що? Яка ще ліц..."
    show iv 2
    St "Йой, вже так пізно!"
    St "Бувай!"
    image bg black = "#070000"

    scene bg black
    show a01
    pause 0.5
    scene bg black
    show a02
    pause 0.5

    scene bg black
    show a0 at center:
        zoom 0.9

    pause 0.2
    scene bg black
    show a0 at center:
        zoom 0.8

    pause 0.2
    scene bg black
    show a0 at center:
        zoom 0.7

    pause 0.5

    hide a02
    pause 0.3
    scene bg black
    show a04
    pause 0.3
    scene bg black
    show a05
    pause 0.3
    scene bg black
    show a06
    pause 0.3

    scene bg black
    show a07:
        xpos 0
        ypos 0
        parallel:
            block:
                ease 0.3:
                    yoffset -100
                ease 0.3:
                    yoffset 100
                repeat
        parallel:
            pause 1
            ease 6.0:
                yalign -1.0
                xpos -1.0
                zoom -1.0
        


    pause 5
    scene bg black with dissolve

    image big_text = ParameterizedText(xalign=0.5, yalign=0.5, size=120, color="#ffffff")

    show big_text "Кінець" with Dissolve(2)

    pause
    return

label the_end_2:
    show st 22
    Iv "Я слухаю. А… Так… Угу…"
    Iv "Ні, я… Так. Так. Так. Ні. Так. А… Ні."
    show st 22_1
    Iv "Я можу завтра."
    Iv "В сенсі? Чому?"
    Iv "Добр… "
    show st 22_2
    Iv "Ох."
    Iv "Мабуть…"
    Iv "…"
    Iv "Добре. До десятої."
    Iv "…"
    show st 20
    St "Щось сталось?"
    Iv "Замовник дзвонив. Хоче отримати готову роботу от прямо зараз і не секундою пізніше."
    St "А то що?"
    show st 20_3
    Iv "А то буду я харчуватись пацюками з каналізації, а не продуктами з супермаркета."
    St "Не заплатить?"
    show st 18
    Iv "Не заплатить."
    St "Я зрозумів. Нічого страшного, значить, сьогодні закінчимо раніше."
    show st 8
    Iv "Пройдешся зі мною до зупинки?"
    St "Звісно. Як я можу тобі відмовити?"
    Iv "Я навіть можу понести твою парасолю."
    St "Тоді мені доведеться понести тебе."
    show st 11_1
    Iv "Я не проти."
    St "Та я, насправді, теж."
    jump end_game_transition

label the_end_3:
    play music "night-jazz-111372.mp3"
    scene bg the end 1 with dissolve
    pause 5.0
    scene bg the end 2 with dissolve
    pause 5.0
    scene bg the end 3 with dissolve
    pause 5.0
    scene bg the end 4 with dissolve
    pause 5.0
    scene bg the end 5 with dissolve
    pause 5.0
    scene bg the end 6 with dissolve
    pause 5.0
    scene bg the end 7 with dissolve
    pause 5.0
    scene bg the end 8 with dissolve
    pause 5.0
    scene bg the end 9 with dissolve
    pause 5.0
    scene bg the end 10 with dissolve
    pause 5.0
    scene bg the end 11 with dissolve
    pause 5.0
    scene bg the end 12 with dissolve
    pause 5.0
    scene bg the end 13 with dissolve
    pause 5.0
    scene bg the end 14 with dissolve
    pause 5.0
    scene bg the end 15 with dissolve
    pause 5.0
    jump end_game_transition

label the_end_4:
    play music "night-jazz-111372.mp3"
    scene bg the end 1 with dissolve
    pause 5.0
    scene bg the end 2 with dissolve
    pause 5.0
    scene bg the end 3 with dissolve
    pause 5.0
    scene bg the end 4 with dissolve
    pause 5.0
    scene bg the end 5 with dissolve
    pause 5.0
    scene bg the end 6 with dissolve
    pause 5.0
    scene bg the end 7 with dissolve
    pause 5.0
    scene bg the end 13 with dissolve
    pause 5.0
    scene bg the end 14 with dissolve
    pause 5.0
    scene bg the end 15 with dissolve
    pause 5.0


label end_game_transition:
    scene bg the end 15 with dissolve:
        blur 90

    image big_text = ParameterizedText(xalign=0.5, yalign=0.5, size=120, color="#ffffff")

    show big_text "Кінець" with Dissolve(2)

    pause
    return