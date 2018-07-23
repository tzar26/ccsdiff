def get__blocks(text):
	"""
	разбивает блок для селектора и правил, разбивая на блоки если несколько селекторов
	"""
	yield ''


def normalize_css(text):
	"""
	нормализует контент стилей перед парсингом:
	- тримит строки на пробелы и табуляторы

	:param text:
	:return str: пример, '.kek{rul:kek;}'
	"""
	return ''


def get__genom(text):
	"""
	из нормализованного блока возвращает пару (селектор, правила)

	:param text: str, например, '.kek{rul:kek;}'
	:return tuple: в указанном примере ('.kek', {'rul': ['kek']})
	"""
	return , {}


def add_rules(rules1, rules2):
	"""
	возвращает результат добавления отсутствующих правил

	:param rules1: dict
	:param rules2: dict
	:return dict:
	"""
	return ''


def get__css_obj(text):
	"""
	возвращает словарь, ключами которого являются селекторы, значения - нормализованные правила
	"""
	css = {}
	blocks = get__blocks(text)
	for block in blocks:
		selector, rules = get__genom(block)
		css[selector] = add_rules(css.get(selector), rules)
	return css
