var cats = []
$.each($('.main_cats a'), function (index, value) {
    var item = $(value).children('div')
    var id = item.attr('id-sub-cat')
    var data = {
        'title': item.text().trim(),
        'id': id,
    };
    var sub_children = $('.sub_navbar_category .sub_cat[sub-cat="' + id + '"]').find('.row a');
    var children = [];
    $.each(sub_children, function (child_index, child_item) {
        children.push({
            'title': $(child_item).text().trim(),
        })
    })
    data['children'] = children
    cats.push(data)
})