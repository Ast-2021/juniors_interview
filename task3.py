def get_the_intersections_of_intervals(interval_1, interval_2):
    """Получить пересечения"""
    idx_1 = 0
    idx_2 = 0
    intersections = []
    while idx_1 < len(interval_1) and idx_2 < len(interval_2):
        start_1, end_1 = interval_1[idx_1]
        start_2, end_2 = interval_2[idx_2]
        
        if end_1 >= start_2 and end_2 >= start_1:
            intersections.append((max(start_1, start_2), min(end_1, end_2)))
        if end_1 < end_2:
            idx_1 += 1
        else:
            idx_2 += 1
    return intersections


def get_intersections_within_a_lesson(intersections, lesson_interval):
    """Получить пересечения в диапазоне начала и конца урока"""
    start_lesson, end_lesson = lesson_interval
    intersections_within_lesson = []
    for start, end in intersections:
        if end > start_lesson and start < end_lesson:
            intersections_within_lesson.append((max(start, start_lesson), min(end, end_lesson)))
    return intersections_within_lesson

def merge_intersections(intervals): 
    """Объединение накладывающихся друг на друга интервалов""" 
    merged = [] 
    for interval in intervals: 
        if not merged or merged[-1][1] < interval[0]: 
            merged.append(interval) 
        else: 
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1])) 
    return merged

def sum_of_all_intersections(intervals):
    """Сумма всех пересечений"""
    total = 0
    for start, end in intervals:
        total += end - start
    return total


def appearance(intervals: dict[str, list[int]]) -> int:

    lesson_interval = intervals['lesson']
    pupil_intervals = [(intervals['pupil'][i], intervals['pupil'][i+1]) for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals = [(intervals['tutor'][i], intervals['tutor'][i+1]) for i in range(0, len(intervals['tutor']), 2)]
    
    intersections = get_the_intersections_of_intervals(pupil_intervals, tutor_intervals)
    intersections_within_lesson = get_intersections_within_a_lesson(intersections, lesson_interval)
    without_intersecting_intervals = merge_intersections(intersections_within_lesson)
    return sum_of_all_intersections(without_intersecting_intervals)
    

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    