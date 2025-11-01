"""
Languages
Estimate: 20 minutes
Actual:   16 minutes
"""

from prac_06.programming_language import ProgrammingLanguage
def main():
    """Create a list of languages, print them out, and identify the languages with dynamic typing"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)
    program_languages =[ProgrammingLanguage("Python", "Dynamic", True, 1991),
                        ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                        ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
    print("The dynamically typed languages are:")
    for language in program_languages:
        if language.is_dynamic():
            print(language.name)


main()