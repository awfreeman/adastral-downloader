from langs.en import en
from langs.fr import fr
from langs.es import es
from langs.it import it
from langs.el import el
from langs.hu import hu
from langs.pl import pl
import locale

langs = {
    "en": en,
    "fr": fr,
    "es": es,
    "it": it,
    "el": el,
    "hu": hu,
    "pl": pl
}

lang = langs["en"]

locale = locale.getdefaultlocale()[0]
if locale in langs:
    lang.update(langs[locale])
elif locale.split("_")[0] in langs:
    lang.update(langs[locale.split("_")[0]])