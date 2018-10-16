$remove = $('#remove');

$(document).ready(function() {


          $('#table').bootstrapTable({
            columns: [
                {
                    title: 'Person',
                    field: 'person_code',
                    sortable: true,
                },
                {
                    title: 'Miao',
                    field: 'material_name',
                    sortable: true,
                },
                {
                    title: 'Rental date',
                    field: 'date_rental',
                    sortable: true
                },
                {
                    title: 'Return date',
                    field: 'date_return',
                    sortable: true
                },
                {
                    title: 'Price',
                    field: 'price',
                    sortable: true
                },
                {
                    title: 'Deposit',
                    field: 'deposit',
                    sortable: true
                },
                {
                    title: 'Notes',
                    field: 'notes',
                    sortable: true
                },
                {
                    field: 'id',
                    events: operateEvents,
                    formatter: operateFormatter
                },
            ]

        });


     function getIdSelections() {
            return $.map($('#table').bootstrapTable('getSelections'), function (row) {
                return row.id
            });
     }

$remove.click(function () {
    var ids = getIdSelections();
    $('#table').bootstrapTable('remove', {
        field: 'id',
        values: ids
    });
    $remove.prop('disabled', true);
});

function operateFormatter(value, row, index) {
        return [
            '<a class="remove" href="javascript:void(0)" title="Remove">',
            '<i class="glyphicon glyphicon-remove"></i>',
            '</a>'
        ].join('');
    }

function detailFormatter(index, row) {
        var html = [];
        $.each(row, function (key, value) {
            html.push('<p><b>' + key + ':</b> ' + value + '</p>');
        });
        return html.join('');
    }




} );

window.operateEvents = {
        'click .remove': function (e, value, row, index) {
            $('#table').bootstrapTable('remove', {
                field: 'id',
                values: [row.id]
            });
        }
    };



