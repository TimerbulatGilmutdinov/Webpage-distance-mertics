import Utils as utils
from nltk.corpus import stopwords
from Cosinus import calculate_cosinus
from Jaccard import calculate_jaccard


science_keywords_dataset = "physics chemistry mathematics biology knowledge school scientist professor scientific teaching teacher study teach university experience history research book discovery laboratory institute philosophy astronomy space geography experiment technique mind progress life study formula study medicine textbook subject microscope thesis brain Newton theory psychology Einstein bathrobe geometry invention granite work man lesson technology people smart doctor algebra computer science glasses mind student academician anatomy Lomonosov philology work student botany zoology literature language brains diploma award academy hypothesis"
sport_keywords_dataset = "football running basketball athlete health volleyball ball hockey competition game olympics tennis strength coach swimming skiing boxing victory training jumping life sports champion medal chess muscles sneakers athletics match barbell championship injury physical education referee team gymnastics stadium gym golf dance skates fitness biathlon racket exercise gym rugby wrestling dumbbells bicycle sweat handball exercise simulator goal water record reward press finish form tournament man labor athlete start gate hockey stick muscles fans cup puck doping movement rope speed cycling endurance spirit time"
shopping_keywords_dataset = "purchases shop money clothes things goods shoes shop waste girl dress bag clothes packages buy illness shoes sale boutique girlfriends seller discounts woman price supermarket gifts Milan map center buyer Sale fashion layout dollar boots joy New York fetishism fitting room fool wife action lady purse handbag chicks waste restaurant Shopping Walking Marketing Consumption Entertainment Pleasure Husband Check Glasses Fur Coat Brand City Cash Desk Mania Brands Camping Time Hat Youth Society"
news_keywords_dataset = "tv newspaper news radio channel internet politics weather bad good TV war media ukraine magazine news new presenter events gossip watch time interview information journalist people program press telephone president fresh sport assassination interesting presenter fire russia read listen world new letter article country news report reporter of the day Putin receive a conversation interesting incidents house life book camera joy advertising premiere announcement evening new mail rumors fear announcer knowledge truth death story sensation message Crimea lie morning tape reason facts"

science_words_list = science_keywords_dataset.split()
sport_words_list = sport_keywords_dataset.split()
shopping_words_list = shopping_keywords_dataset.split()
news_words_list = news_keywords_dataset.split()

print("Input language of the web page")
language = str(input())
stop_words = list(stopwords.words(language))

utils.remove_stop_words(stop_words, science_words_list)
utils.remove_stop_words(stop_words, sport_words_list)
utils.remove_stop_words(stop_words, shopping_words_list)
utils.remove_stop_words(stop_words, news_words_list)

print("Enter a link to the web page")
url = str(input())
# An example of web page
# url = 'https://edition.cnn.com/2023/04/11/sport/helen-maroulis-concussion-wrestling-spt-intl/index.html'
text = utils.get_page_text(url)
text = text.lower()
text_as_vector = utils.text_to_vector(text)
text = text.split()

utils.remove_stop_words(stop_words, text)

science_vector = utils.text_to_vector(science_keywords_dataset)
sport_vector = utils.text_to_vector(sport_keywords_dataset)
shopping_vector = utils.text_to_vector(shopping_keywords_dataset)
news_vector = utils.text_to_vector(news_keywords_dataset)

print("Cosinus metrics")
print(f"Science: {calculate_cosinus(text_as_vector, science_vector)}")
print(f"Sport: {calculate_cosinus(text_as_vector, sport_vector)}")
print(f"Shopping: {calculate_cosinus(text_as_vector, shopping_vector)}")
print(f"News: {calculate_cosinus(text_as_vector, news_vector)}")

print("Jaccard metrics")
print(f"Science: {calculate_jaccard(text, science_words_list)}")
print(f"Sport: {calculate_jaccard(text, sport_words_list)}")
print(f"Shopping: {calculate_jaccard(text, shopping_words_list)}")
print(f"News: {calculate_jaccard(text, news_words_list)}")
