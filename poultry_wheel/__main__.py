from dearpygui.core import *
from dearpygui.simple import *
from datetime import date, timedelta


class App:
    def __init__(self):
        pass

    @property
    def age_list(self):
        return [int(i.strip()) for i in get_value('##age_list').split(',')]

    def calculate(self, sender, data):
        clear_table('##output_table')
        hatch_date = date(int(get_value('##year')),
                          int(get_value('##month')),
                          int(get_value('##day')))

        dates = {i: hatch_date + timedelta(weeks=i)
                 for i in self.age_list}

        for k, v in dates.items():
            add_row('##output_table', [k, v])

    def show(self):
        with window('##main_window'):
            set_main_window_title('Poultry Wheel')
            set_main_window_size(300, 350)

            # age list
            add_input_text('##age_list', width=268,
                           hint='Age List (comma sep)')

            # date
            date_width = 84
            add_input_text('##year', hint='year', width=date_width)
            add_same_line()
            add_input_text('##month', hint='month', width=date_width)
            add_same_line()
            add_input_text('##day', hint='day', width=date_width)

            # calculate
            add_button('Calculate', callback=self.calculate,
                       width=268, height=25)

            # table
            add_table('##output_table', ['Age', 'Date'])

        start_dearpygui(primary_window='##main_window')


if __name__ == '__main__':
    app = App()
    app.show()
