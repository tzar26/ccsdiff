from cssdiff import normalize_css, get__blocks


class TestGetBlocks:
	def test__parse_to_blocks(self):
		"""
		.kek, .lol {
			rul1: 1;
			rul2: 2;
		}
		.azaza za {rul3: 3 4;} => [.kek{rul1:1;rul2:2;}, .kek{rul1:1;rul2:2;}, .azaza za{rul3:3 4;}]
		"""
		data = """
		.kek, .lol {rul1: 1;rul2: 2;}
		.azaza za {rul3: 3 4;}"""
		result_list = list(get__blocks(data))
		expected_list = ['.kek{rul1:1;rul2:2;}', '.kek{rul1:1;rul2:2;}', '.azaza za{rul3:3 4;}']
		assert expected_list[0] in result_list
		assert expected_list[1] in result_list
		assert expected_list[2] in result_list
		assert result_list[0] in expected_list
		assert result_list[1] in expected_list
		assert result_list[2] in expected_list

	def test__parse__with_media(self):
		"""
		@media (max-width: 767px) {
			.page-kek nav {
				display: none;
			}

			.page-kek + footer {
				display: none;
			}
		} => [
				@media (max-width: 767px)&&.page-kek nav{display:none;},
				@media (max-width: 767px)&&.page-kek + footer{display:none;}
			]
		"""
		data = """@media (max-width: 767px) {
			.page-kek nav {display: none;}

			.page-kek + footer {display: none;}
		}"""
		result_list = list(get__blocks(data))
		expected_list = [
			'@media (max-width: 767px)&&.page-kek nav{display:none;}',
			'@media (max-width: 767px)&&.page-kek + footer{display:none;}'
		]
		assert expected_list[0] in result_list
		assert expected_list[1] in result_list
		assert result_list[0] in expected_list
		assert result_list[1] in expected_list


class TestNormalizeCSS:
	def test__normalize(self):
		"""
		тестируем сжатие контента за счёт удаления лишних пробелов и табуляторов и
		добавление отсутствующего ";" у правила
		"""
		data =  """		 .kek {		rul:   kek
		}
		"""
		expected = '.kek{rul:kek;}'
		assert normalize_css(data) == expected

	def test__normalize_with_media(self):
		"""
		тестируем свёртку медиа и селектора и дополнени правила знаком ";" на конце
		"""
		data = """
		@media (max-width: 767px)&&.page-kek nav {
				display: none
			}
		"""
		expected = '@media (max-width: 767px)&&.page-kek nav{display:none;}'
		assert normalize_css(data) == expected


class TestGetGenom:
	def test1(self):
		pass
