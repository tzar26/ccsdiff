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
	:return str:
	"""
	return ''


def get__genom(text):
	"""
	из нормализованного блока возвращает пару (селектор, правила)
	"""
	return ,


def add_rules(rules1, rules2):
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
