from django import template


register = template.Library()


@register.filter
def status_class(value):
    return {
        "new": "status-new",
        "scheduled": "status-scheduled",
        "completed": "status-completed",
    }.get(value, "status-muted")


@register.filter
def room_image(value):
    return {
        "auditorium": "img/media/1679169355_design-pibig-info-p-sovr_jpg.webp",
        "coworking": "img/media/dizayn-interera-co-working-_jpg.webp",
        "cinema": "img/media/1643087798_5-bigfoto-name-p-id_jpg.webp",
    }.get(value, "img/media/yerinde-temizlik_jpg.webp")

