new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# удалена task_005 из списка new_tasks и добавлена в список completed_tasks
completed_tasks.append(new_tasks.pop())

# удалена task_007 из списка new_tasks
new_tasks.remove('task_007')

# вывод последней таски из списка new_tasks
print(new_tasks[len(new_tasks) - 1])
