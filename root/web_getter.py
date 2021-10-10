import requests
from bs4 import BeautifulSoup


class Web_Getter:
    def _get_text(self, variant, task) -> str:
        r = requests.get('https://fizikadlyvas.ru/'
                       'ege-2021-po-russkomu-yazyku-tipovye-ekzamenatsionnye-varianty-i-p-tsybulko-36-variantov-variant-'
                       '{variant}-zadanie-{task}'.format(variant=variant, task=task))
        html = BeautifulSoup(r.content, 'html.parser')
        return str(html.find('div', {'class': 'bd-productdesc-13'}).text)

    def get_variant_text(self, task) -> list[str]:
        variants = [None]
        for variant in range(1, 37):
            variants.append(self._get_text(variant=variant, task=task))
        return variants
