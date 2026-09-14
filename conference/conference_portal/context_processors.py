GALLERY_IMAGES = [
    {
        "src": "img/media/12fe2c7de382debb49c_jpg.webp",
        "alt": "Лекторий с мягкими местами",
        "caption": "Лекторий",
    },
    {
        "src": "img/media/1643087798_5-bigfoto-name-p-id_jpg.webp",
        "alt": "Кинозал с креслами-мешками",
        "caption": "Кинозал",
    },
    {
        "src": "img/media/1679169355_design-pibig-info-p-sovr_jpg.webp",
        "alt": "Конференц-зал с экраном",
        "caption": "Аудитория",
    },
    {
        "src": "img/media/2692984_1632745507.225_jpg.webp",
        "alt": "Зал для докладов",
        "caption": "Зал докладов",
    },
    {
        "src": "img/media/5622ba05cc6857865cfa_jpg.webp",
        "alt": "Коворкинг с зелеными диванами",
        "caption": "Коворкинг",
    },
    {
        "src": "img/media/7621e0c3c1df2e3322f6222ff94e67f3_jpg.webp",
        "alt": "Открытая рабочая зона",
        "caption": "Рабочая зона",
    },
    {
        "src": "img/media/864c66af3dc2cc0eb8166ba359500f25_jpg.webp",
        "alt": "Учебная аудитория с проектором",
        "caption": "Аудитория",
    },
    {
        "src": "img/media/978e0d84d6b940fe1_jpg.webp",
        "alt": "Современное пространство с лестницей",
        "caption": "Пространство",
    },
    {
        "src": "img/media/ad4b1ceed37823f2225c0e7a_jpg.webp",
        "alt": "Светлая переговорная",
        "caption": "Переговорная",
    },
    {
        "src": "img/media/c522e46c4a9682fdebb_jpg.webp",
        "alt": "Аудитория с модульными местами",
        "caption": "Амфитеатр",
    },
    {
        "src": "img/media/diploma_webp.webp",
        "alt": "Круговая переговорная",
        "caption": "Круглый зал",
    },
    {
        "src": "img/media/dizayn-interera-co-working-_jpg.webp",
        "alt": "Конференц-пространство с экраном",
        "caption": "Конференц-зал",
    },
    {
        "src": "img/media/e0aa2a26192b2d5bd69_jpg.webp",
        "alt": "Аудитория с деревянной отделкой",
        "caption": "Аудитория",
    },
    {
        "src": "img/media/ec8a14264510f22a979f3_jpg.webp",
        "alt": "Лекторий с зелеными рядами",
        "caption": "Лекторий",
    },
    {
        "src": "img/media/etazhi-logotip-vektor-48_jpg.webp",
        "alt": "Графический знак здания",
        "caption": "Площадка",
    },
    {
        "src": "img/media/imgbin-orange_jpg.webp",
        "alt": "Графический знак сервиса",
        "caption": "Сервис",
    },
    {
        "src": "img/media/praktik-nevskogo-spb-kovorkin_jpg.webp",
        "alt": "План и фотографии коворкинга",
        "caption": "План коворкинга",
    },
    {
        "src": "img/media/tomas-blog_png.webp",
        "alt": "Коворкинг с рабочими столами",
        "caption": "Рабочие места",
    },
    {
        "src": "img/media/unnamed_jpg.webp",
        "alt": "Аудитория с черными креслами",
        "caption": "Аудитория",
    },
    {
        "src": "img/media/XXL_height_webp.webp",
        "alt": "Офисное пространство в индустриальном стиле",
        "caption": "Коворкинг",
    },
    {
        "src": "img/media/yerinde-temizlik_jpg.webp",
        "alt": "Яркий коворкинг с переговорными",
        "caption": "Коворкинг",
    },
]

SOCIAL_IMAGES = [
    {
        "src": "img/social/soc_png.webp",
        "alt": "VK и Одноклассники",
    },
    {
        "src": "img/social/social_jpg.webp",
        "alt": "Социальные сети VK и Одноклассники",
    },
    {
        "src": "img/social/social_png.webp",
        "alt": "Иконки социальных сетей",
    },
]

ROOM_IMAGES = {
    "auditorium": "img/media/1679169355_design-pibig-info-p-sovr_jpg.webp",
    "coworking": "img/media/dizayn-interera-co-working-_jpg.webp",
    "cinema": "img/media/1643087798_5-bigfoto-name-p-id_jpg.webp",
}


def design_assets(request):
    return {
        "brand_mark": "img/media/1282150_png.webp",
        "hero_image": "img/media/yerinde-temizlik_jpg.webp",
        "gallery_images": GALLERY_IMAGES,
        "social_images": SOCIAL_IMAGES,
        "room_images": ROOM_IMAGES,
    }

