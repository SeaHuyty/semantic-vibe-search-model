## Base Sentence Transformer Model, No Finetuning
Sentence Transformer model: all-MiniLM-L6-v2 with 384 dimensions.

## Test Query and Result

Query: happy anniversary
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist             ┃ Song                      ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Vera Lynn          │ Anniversary Waltz         │ 0.5043 │
│    2 │ Tom T. Hall        │ Little Green Flower With  │ 0.4357 │
│      │                    │ The Yellow On Top         │        │
│    3 │ Louis Armstrong    │ Congratulations To        │ 0.4336 │
│      │                    │ Someone                   │        │
│    4 │ Lionel Richie      │ Three Times A Lady        │ 0.4207 │
│    5 │ Michael Jackson    │ Happy Birthday Lisa       │ 0.4167 │
│    6 │ Ocean Colour Scene │ Golden Gate Bridge        │ 0.4131 │
│    7 │ George Jones       │ As Long As We Can         │ 0.4126 │
│    8 │ Carol Banawa       │ All The Years             │ 0.4105 │
│    9 │ Cliff Richard      │ Congratulations           │ 0.4089 │
│   10 │ Mary Black         │ Moments                   │ 0.4019 │
└──────┴────────────────────┴───────────────────────────┴────────┘

Query: party anthem for a Friday night club
                     Search Results                      
┏━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist        ┃ Song                  ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Lionel Richie │ All Night Long        │ 0.5462 │
│    2 │ Roy Orbison   │ Good Time Party       │ 0.5335 │
│    3 │ Human League  │ Party                 │ 0.5176 │
│    4 │ Alabama       │ Gonna Have A Party    │ 0.5100 │
│    5 │ Poison        │ Power To The People   │ 0.5062 │
│    6 │ Warren Zevon  │ The Rest Of The Night │ 0.4951 │
│    7 │ Madonna       │ Celebration           │ 0.4924 │
│    8 │ Wiz Khalifa   │ No Sleep              │ 0.4883 │
│    9 │ R. Kelly      │ It's Your Birthday    │ 0.4876 │
│   10 │ Eurythmics    │ Party Town            │ 0.4861 │
└──────┴───────────────┴───────────────────────┴────────┘

Query: sad piano song about losing someone
                          Search Results
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist                ┃ Song                   ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Nightwish             │ Dead Boy's Poem        │ 0.6242 │
│    2 │ Hank Snow             │ Born To Lose           │ 0.5992 │
│    3 │ Engelbert Humperdinck │ Dancing With Tears In  │ 0.5930 │
│      │                       │ My Eyes                │        │
│    4 │ George Strait         │ Blue Melodies          │ 0.5874 │
│    5 │ Roy Orbison           │ Only Alive             │ 0.5844 │
│    6 │ Oasis                 │ Headshrinker           │ 0.5795 │
│    7 │ Carpenters            │ Hits Medley '76        │ 0.5785 │
│    8 │ Loretta Lynn          │ Once A Day             │ 0.5767 │
│    9 │ Engelbert Humperdinck │ The Way It Used To Be  │ 0.5729 │
│   10 │ Utada Hikaru          │ For You                │ 0.5688 │
└──────┴───────────────────────┴────────────────────────┴────────┘

Query: chill lo-fi vibe for studying
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist            ┃ Song                       ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ 'n Sync           │ James Rusionz              │ 0.4442 │
│    2 │ Kanye West        │ School Spirit Skit         │ 0.4275 │
│    3 │ Paul Simon        │ Kodachrome                 │ 0.4137 │
│    4 │ Judy Garland      │ All God's Chillun Got      │ 0.3898 │
│      │                   │ Rhythm                     │        │
│    5 │ Ian Hunter        │ Cool                       │ 0.3881 │
│    6 │ Steve Miller Band │ Hot Chili                  │ 0.3755 │
│    7 │ Glee              │ Cool                       │ 0.3692 │
│    8 │ Grease            │ Back To School Again       │ 0.3631 │
│    9 │ Glee              │ Hot For Teacher            │ 0.3623 │
│   10 │ Roxette           │ Physical Fascination       │ 0.3597 │
└──────┴───────────────────┴────────────────────────────┴────────┘

Query: christmas holiday cheer song
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist           ┃ Song                        ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Christmas Songs  │ Christmas Day               │ 0.6522 │
│    2 │ Michael W. Smith │ Christmas Day               │ 0.6488 │
│    3 │ Christmas Songs  │ If Every Day Was Like       │ 0.6424 │
│      │                  │ Christmas                   │        │
│    4 │ Train            │ Shake up Christmas          │ 0.6371 │
│    5 │ Perry Como       │ C-h-r-i-s-t-m-a-s           │ 0.6191 │
│    6 │ Kenny Loggins    │ On Christmas Morning        │ 0.6187 │
│    7 │ Alabama          │ Happy Holidays              │ 0.6172 │
│    8 │ Michael W. Smith │ The Happiest Christmas      │ 0.6121 │
│    9 │ Oasis            │ Merry Christmas             │ 0.6090 │
│   10 │ King Diamond     │ Christmas                   │ 0.6081 │
└──────┴──────────────────┴─────────────────────────────┴────────┘

Query: motivational workout gym anthem
                          Search Results                          
┏━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist          ┃ Song                         ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Utada Hikaru    │ The Workout                  │ 0.4856 │
│    2 │ Cyndi Lauper    │ Baby Workout                 │ 0.4626 │
│    3 │ Mc Hammer       │ 2 Legit 2 Quit               │ 0.4553 │
│    4 │ Flo-Rida        │ Marching On                  │ 0.4542 │
│    5 │ Pitbull         │ Game On                      │ 0.4513 │
│    6 │ Imperials       │ Trumpet Of Jesus             │ 0.4424 │
│    7 │ Vanilla Ice     │ Ice Is Workin' It            │ 0.4367 │
│    8 │ R. Kelly        │ Like I Do                    │ 0.4289 │
│    9 │ Ten Years After │ Rock Roll Music To The World │ 0.4246 │
│   10 │ Rihanna         │ Vogue                        │ 0.4189 │
└──────┴─────────────────┴──────────────────────────────┴────────┘

Query: patriotic song about war and sacrifice
                       Search Results                        
┏━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Rank ┃ Artist        ┃ Song                      ┃  Score ┃
┡━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    1 │ Cliff Richard │ From A Distance           │ 0.6040 │
│    2 │ Black Sabbath │ Anno Mundi                │ 0.5867 │
│    3 │ Iron Maiden   │ These Colours Don't Run   │ 0.5829 │
│    4 │ UB40          │ Sing Our Own Song         │ 0.5816 │
│    5 │ Matt Redman   │ We Are The Free           │ 0.5808 │
│    6 │ Indigo Girls  │ Finlandia                 │ 0.5798 │
│    7 │ Reba Mcentire │ All The Soldiers Are Dead │ 0.5788 │
│    8 │ Arlo Guthrie  │ Patriot's Dream           │ 0.5786 │
│    9 │ Ray Charles   │ America The Beautiful     │ 0.5749 │
│   10 │ Donna Summer  │ From A Distance           │ 0.5745 │
└──────┴───────────────┴───────────────────────────┴────────┘