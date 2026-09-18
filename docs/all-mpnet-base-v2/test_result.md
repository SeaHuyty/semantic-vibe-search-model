## Base Sentence Transformer Model, No Finetuning
Sentence Transformer model: all-mpnet-base-v2 with 768 dimensions.

## Test Query and Result

Query: "happy anniversary"
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist             ┃ Song                      ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Vera Lynn          │ Anniversary Waltz         │ 0.5150 │
│    2 │ George Jones       │ As Long As We Can         │ 0.4509 │
│    3 │ John Denver        │ For You                   │ 0.4467 │
│    4 │ Ocean Colour Scene │ Golden Gate Bridge        │ 0.4450 │
│    5 │ Tom T. Hall        │ Little Green Flower With  │ 0.4445 │
│      │                    │ The Yellow On Top         │        │
│    6 │ Arlo Guthrie       │ Wedding Song              │ 0.4437 │
│    7 │ Steve Miller Band  │ Shangri-la                │ 0.4361 │
│    8 │ Lionel Richie      │ Three Times A Lady        │ 0.4335 │
│    9 │ Chicago            │ Love Was New              │ 0.4248 │
│   10 │ Olivia Newton-John │ Making A Good Thing       │ 0.4238 │
│      │                    │ Better                    │        │
└──────┴────────────────────┴───────────────────────────┴────────┘

Query: "party anthem for a Friday night club"
                        Search Results                        
┏━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist        ┃ Song                       ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ One Direction │ I Gotta Feeling            │ 0.6490 │
│    2 │ Miley Cyrus   │ Let's Dance                │ 0.6294 │
│    3 │ Quiet Riot    │ Party All Night            │ 0.6226 │
│    4 │ Kiss          │ Shout It Out Loud          │ 0.6158 │
│    5 │ Who           │ Saturday Night's Alright   │ 0.6115 │
│    6 │ Roy Orbison   │ Good Time Party            │ 0.6068 │
│    7 │ Miley Cyrus   │ We Got The Party (With Us) │ 0.5848 │
│    8 │ Gloria Gaynor │ Anybody Wanna Party?       │ 0.5845 │
│    9 │ Lionel Richie │ All Night Long             │ 0.5830 │
│   10 │ Human League  │ Party                      │ 0.5791 │
└──────┴───────────────┴────────────────────────────┴────────┘

Query: "sad piano song about losing someone"
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist                ┃ Song                   ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Quasi                 │ Two By Two             │ 0.6518 │
│    2 │ Hanson                │ Cried                  │ 0.6438 │
│    3 │ Mariah Carey          │ Bye Bye                │ 0.6435 │
│    4 │ Engelbert Humperdinck │ The Way It Used To Be  │ 0.6382 │
│    5 │ Loretta Lynn          │ I Need Someone To Hold │ 0.6377 │
│      │                       │ Me (When I Cry)        │        │
│    6 │ HIM                   │ Bury Me Deep Inside    │ 0.6292 │
│      │                       │ Your Heart             │        │
│    7 │ Alison Krauss         │ Sitting In The Window  │ 0.6279 │
│      │                       │ Of My Room             │        │
│    8 │ Doobie Brothers       │ Take Me In Your Arms   │ 0.6253 │
│    9 │ Nightwish             │ Dead Boy's Poem        │ 0.6210 │
│   10 │ X                     │ Dancing With Tears In  │ 0.6152 │
│      │                       │ My Eyes                │        │
└──────┴───────────────────────┴────────────────────────┴────────┘

Query: "chill lo-fi vibe for studying"
                       Search Results                       
┏━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist        ┃ Song                     ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Hooverphonic  │ Electro Shock Faders     │ 0.4293 │
│    2 │ Boney M.      │ Sample City              │ 0.4044 │
│    3 │ 'n Sync       │ James Rusionz            │ 0.3795 │
│    4 │ Ramones       │ Rock 'n Roll High School │ 0.3716 │
│    5 │ Oingo Boingo  │ Cool City                │ 0.3646 │
│    6 │ Clash         │ Cool Under Heat          │ 0.3645 │
│    7 │ Jimmy Buffett │ Domino College           │ 0.3577 │
│    8 │ Clash         │ Overpowered By Funk      │ 0.3502 │
│    9 │ Enigma        │ Look Of Today            │ 0.3384 │
│   10 │ Venom         │ Darkest Realm            │ 0.3342 │
└──────┴───────────────┴──────────────────────────┴────────┘

Query: "christmas holiday cheer song"
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist             ┃ Song                      ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Train              │ Shake up Christmas        │ 0.7363 │
│    2 │ Christina Aguilera │ Christmas Time            │ 0.7233 │
│    3 │ Bing Crosby        │ Christmas Is              │ 0.7102 │
│    4 │ Raffi              │ Every Little Wish         │ 0.6956 │
│    5 │ Lady Gaga          │ Christmas Tree            │ 0.6921 │
│    6 │ Faith Hill         │ Holly Jolly Christmas     │ 0.6883 │
│    7 │ Justin Bieber      │ Christmas Love            │ 0.6761 │
│    8 │ Vonda Shepard      │ Please Come Home For      │ 0.6743 │
│      │                    │ Christmas                 │        │
│    9 │ Christmas Songs    │ On Christmas Morning      │ 0.6740 │
│   10 │ Michael W. Smith   │ The Happiest Christmas    │ 0.6733 │
└──────┴────────────────────┴───────────────────────────┴────────┘

Query: "motivational workout gym anthem"
                       Search Results                       
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist            ┃ Song                 ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Cyndi Lauper      │ Baby Workout         │ 0.5798 │
│    2 │ Journey           │ What It Takes To Win │ 0.5385 │
│    3 │ Mc Hammer         │ 2 Legit 2 Quit       │ 0.5357 │
│    4 │ Quiet Riot        │ Main Attraction      │ 0.5355 │
│    5 │ Utada Hikaru      │ The Workout          │ 0.5162 │
│    6 │ Spandau Ballet    │ Motivator            │ 0.5160 │
│    7 │ Manowar           │ Number 1             │ 0.5155 │
│    8 │ Michael Jackson   │ Man In The Mirror    │ 0.5123 │
│    9 │ Justin Timberlake │ Follow My Lead       │ 0.5112 │
│   10 │ Pitbull           │ Game On              │ 0.5087 │
└──────┴───────────────────┴──────────────────────┴────────┘

Query: "patriotic song about war and sacrifice"
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist                 ┃ Song                  ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Ray Boltz              │ Fallen Not Forgotten  │ 0.7184 │
│    2 │ Erasure                │ The Soldier's Return  │ 0.6651 │
│    3 │ Uriah Heep             │ Fires Of Hell         │ 0.6593 │
│    4 │ Michael Jackson        │ History               │ 0.6567 │
│    5 │ Nitty Gritty Dirt Band │ Soldier Of Love       │ 0.6464 │
│    6 │ W.A.S.P.               │ War Cry               │ 0.6458 │
│    7 │ Backstreet Boys        │ Soldier               │ 0.6422 │
│    8 │ David Allan Coe        │ Love Is A Never       │ 0.6372 │
│      │                        │ Ending War            │        │
│    9 │ Dolly Parton           │ Brave Little Soldier  │ 0.6334 │
│   10 │ Neil Young             │ Flags Of Freedom      │ 0.6291 │
└──────┴────────────────────────┴───────────────────────┴────────┘

Query: "khmer song 2026"
                      Search Results                       
┏━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist          ┃ Song                  ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Foo Fighters    │ Holiday In Cambodia   │ 0.4882 │
│    2 │ Vangelis        │ State Of Independence │ 0.4557 │
│    3 │ Oasis           │ Manuk Dadali          │ 0.4489 │
│    4 │ Freddie Aguilar │ Anak Pawis            │ 0.4408 │
│    5 │ Who             │ Pure And Easy         │ 0.4404 │
│    6 │ Grease          │ We Go Together        │ 0.4401 │
│    7 │ Kim Wilde       │ Cambodia              │ 0.4390 │
│    8 │ Jose Mari Chan  │ Paskong Kay Ganda     │ 0.4388 │
│    9 │ Ariel Rivera    │ Minamahal Pala Kita   │ 0.4362 │
│   10 │ Freddie Aguilar │ Bulag, Pipi At Bingi  │ 0.4349 │
└──────┴─────────────────┴───────────────────────┴────────┘

Query: "modern k-pop dance track"
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist          ┃ Song                         ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Wilson Phillips │ Dance Dance Dance            │ 0.5061 │
│    2 │ Divine          │ Native Love                  │ 0.5056 │
│    3 │ Kylie Minogue   │ Heart Beat Rock              │ 0.5009 │
│    4 │ Jennifer Lopez  │ Dance Again                  │ 0.5005 │
│    5 │ Beach Boys      │ Dance, Dance, Dance          │ 0.5000 │
│    6 │ Flo-Rida        │ Hey Jasmin                   │ 0.4989 │
│    7 │ Rick Astley     │ Modern Girl                  │ 0.4927 │
│    8 │ Leo Sayer       │ You Make Me Feel Like        │ 0.4922 │
│      │                 │ Dancing                      │        │
│    9 │ Boney M.        │ Kalimba De Luna              │ 0.4791 │
│   10 │ Britney Spears  │ My Song                      │ 0.4789 │
└──────┴─────────────────┴──────────────────────────────┴────────┘

Query: "traditional cambodian wedding music"
                        Search Results                        
┏━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist           ┃ Song                    ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Regine Velasquez │ Kung Maibabalik Ko Lang │ 0.5226 │
│    2 │ Lata Mangeshkar  │ Dil Hoom Hoom Kare      │ 0.5131 │
│    3 │ Yeng Constantino │ Himig Ng Pag-ibig       │ 0.4991 │
│    4 │ Dewa 19          │ Lagu Cinta              │ 0.4893 │
│    5 │ Freestyle        │ Bakit Iniwan Na         │ 0.4799 │
│    6 │ Freddie Aguilar  │ Olongapo                │ 0.4791 │
│    7 │ Regine Velasquez │ Ngayong Wala Ka Na      │ 0.4753 │
│    8 │ Oasis            │ Manuk Dadali            │ 0.4727 │
│    9 │ Dewa 19          │ Aku Cinta Kau Dan Dia   │ 0.4694 │
│   10 │ Perry Como       │ Chincherinchee          │ 0.4680 │
└──────┴──────────────────┴─────────────────────────┴────────┘

Query: "tiktok viral dance sound 2026"
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist          ┃ Song                         ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Prince          │ 2020                         │ 0.4834 │
│    2 │ Wilson Phillips │ Dance Dance Dance            │ 0.4699 │
│    3 │ Beach Boys      │ Dance, Dance, Dance          │ 0.4646 │
│    4 │ Queen Latifah   │ Dance For Me                 │ 0.4580 │
│    5 │ Jimmy Buffett   │ Apocalypso                   │ 0.4505 │
│    6 │ Frank Zappa     │ Be-bop Tango (Of The Old     │ 0.4428 │
│      │                 │ Jazzmen's Church)            │        │
│    7 │ Inna            │ House Is Going On            │ 0.4389 │
│    8 │ LL Cool J       │ I Need A Beat                │ 0.4347 │
│    9 │ Kylie Minogue   │ Speakerphone                 │ 0.4328 │
│   10 │ David Guetta    │ On The Dancefloor            │ 0.4303 │
└──────┴─────────────────┴──────────────────────────────┴────────┘