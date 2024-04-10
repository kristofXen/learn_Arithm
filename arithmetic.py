# write your code here

# def evaluate_string(code: str) -> any:
#     """Can not eval 5+5 from python 3.7 and up"""
#     return ast.literal_eval(code)

# def evaluate(code: str) -> any:
#     # limit access
#     globals_dict = dict()
#     globals_dict['__builtins__'] = dict()
#     locals_dict = dict()
#     return eval(code, globals_dict, locals_dict)

import random


def _get_locally_allowed_names() -> dict:
    allowed_names_in_local = dict()
    allowed_names_in_local['sum'] = sum
    return allowed_names_in_local


def _get_globals_dict() -> dict:
    globals_dict = dict()
    globals_dict['__builtins__'] = dict()
    return globals_dict


def eval_expr(input_str: str) -> any:
    allowed_names_in_local = _get_locally_allowed_names()
    code = compile(input_str, '<string>', 'eval')

    for name in code.co_names:
        if name not in allowed_names_in_local:
            raise NameError(name + ' not allowed in expression')

    return eval(code, _get_globals_dict(), allowed_names_in_local)


# task 2
def _task_setup() -> str:
    nrs = ['2', '3', '4', '5', '6', '7', '8', '9']
    ops = ['*', '-', '+']
    nr1 = random.choice(nrs)
    nr2 = random.choice(nrs)
    op = random.choice(ops)
    return nr1 + ' ' + op + ' ' + nr2


def _task_2_setup() -> str:
    nrs_ = list(range(11, 30))
    nrs = [str(n) for n in nrs_]
    nr = random.choice(nrs)
    return nr + '**2'


# mains #
def main_1_4():
    ui = input()
    print(eval_expr(ui))


def main_2_4():
    task_str = _task_setup()
    print(task_str)
    ui = input()
    if ui == str(eval_expr(task_str)):
        print('Right!')
    else:
        print('Wrong!')

def main_3_4():
    nr_of_tasks = 5
    score = 0

    for _ in range(nr_of_tasks):
        task_str = _task_setup()
        print(task_str)
        correct_form = False
        while not correct_form:
            ui = input()
            try:
                ui_int = int(ui)
                correct_form = True
            except ValueError:
                print('Incorrect format.')
        if ui_int == eval_expr(task_str):
            print('Right!')
            score = score + 1
        else:
            print('Wrong!')
    print('Your mark is ' + str(score) + '/5.')

# 4 - 4 #
def _task_select():
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    ui = input()
    correct_form = False
    while not correct_form:
        try:
            ui_int = int(ui)
            if ui_int not in [1, 2]:
                raise ValueError()
        except ValueError:
            print('Incorrect format.')
        else:
            correct_form = True
    if ui_int == 1:
        return _task_setup, '1', '(simple operations with numbers 2-9)'
    if ui_int == 2:
        return _task_2_setup, '2', '(integral squares of 11-29)'


def _safe_results(score, nr_of_tasks, level, description):
    ui = input()
    if ui.lower() in ['yes', 'y']:
        print('What is your name?')
        name = input()
        with open('./results.txt', 'a') as f:
            f.write(name + ': ' + str(score) + '/' + str(nr_of_tasks)
                    + ' in level ' + level + ' ' + description + '\n')
        print('The results are saved in "results.txt".')
    else:
        pass


def main_4_4():
    task_call, level, description = _task_select()

    nr_of_tasks = 5
    score = 0

    for _ in range(nr_of_tasks):
        task_str = task_call()
        if level == '2':
            task_str_to_print = task_str[:-3]
        else:
            task_str_to_print = task_str
        print(task_str_to_print)
        correct_form = False
        while not correct_form:
            ui = input()
            try:
                ui_int = int(ui)
                correct_form = True
            except ValueError:
                print('Incorrect format.')
        if ui_int == eval_expr(task_str):
            print('Right!')
            score = score + 1
        else:
            print('Wrong!')
    print('Your mark is ' + str(score)
          + '/5. Would you like to save the result? Enter yes or no.')

    _safe_results(score, nr_of_tasks, level, description)



if __name__ == '__main__':
    main_4_4()
