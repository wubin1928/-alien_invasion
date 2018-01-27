import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		"""初始化按钮的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# 设置按钮的尺寸和其他属性
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('幼圆', 50)
		self.font_text = pygame.font.SysFont('幼圆', 17)

		# 创建按钮的rect对象， 并使其居中
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# 按钮的标签只需创建一次
		self.prep_msg(msg)
		self.prep_instructions_text()

	def prep_msg(self, msg):
		"""将msg渲染为图像， 并使其在按钮上居中"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def prep_instructions_text(self):
		"""渲染游戏说明文档"""
		filename = '游戏操作说明.txt'
		with open(filename) as f_obj:
			contents = f_obj.read()
		self.instructions_text = self.font_text.render(contents, True,
												  (0, 0, 0))

		# 将等级放在得分下方
		self.instructions_text_rect = self.instructions_text.get_rect( )
		self.instructions_text_rect.x = 20
		self.instructions_text_rect.y = 660

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		self.screen.blit(self.instructions_text, self.instructions_text_rect)
