class CourseSelectionException(Exception):
    """
    کلاس پایه‌ی همه‌ی استثناهای پروژه.
    هیچ منطق اضافه‌ای ندارد و پیام را همان‌طور که هست نگه می‌دارد.
    """
    pass


# --- Exceptions عمومی/مشترک ---
class ValidationException(CourseSelectionException):
    """خطاهای اعتبارسنجی ورودی‌ها"""
    pass


class NotFoundException(CourseSelectionException):
    """وقتی یک موجودیت پیدا نمی‌شود"""
    pass


class AlreadyExistsException(CourseSelectionException):
    """وقتی رکورد تکراری باشد"""
    pass


class StorageException(CourseSelectionException):
    """خطاهای مربوط به خواندن/نوشتن فایل‌ها یا ذخیره‌سازی"""
    pass


# --- Exceptions مربوط به موجودیت‌ها ---
class StudentException(CourseSelectionException):
    """خطاهای مربوط به عملیات دانشجو"""
    pass


class ProfessorException(CourseSelectionException):
    """خطاهای مربوط به عملیات استاد"""
    pass


class CourseException(CourseSelectionException):
    """خطاهای مربوط به عملیات درس"""
    pass


# --- Exceptions تخصصی انتخاب واحد ---
class CapacityFullException(CourseSelectionException):
    """ظرفیت درس پر است"""
    pass


class AlreadySelectedException(CourseSelectionException):
    """درس قبلاً توسط دانشجو انتخاب شده"""
    pass


class NotSelectedException(CourseSelectionException):
    """درس توسط دانشجو انتخاب نشده که بخواهیم حذف کنیم"""
    pass
