import Formatter, VariableExtractor, sys
from datetime import datetime


def main():
    try:
        with open('input.py', 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f'Error: File Not Found')
        sys.exit(1)

    extractor = VariableExtractor.VariableExtractor()
    variables = extractor.extract(code)
    # issue = RecognizeErrors.recognizeErrors(variables)
    processor = Formatter.ASTProcessor(variables)
    header, column_widths, total_width = processor.generate_header(processor.variables)
    table = processor.generate_table(processor.variables, column_widths, total_width)

    # Prepare output
    output_content = f"\n{'=' * 50}\n"
    output_content += f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    output_content += f"{'-' * 50}\n"  # Adds separator before each run
    output_content += header + table
    output_content += f"{'=' * 50}\n\n"  # Adds separator after each run

    # Write output to file
    output_file_path = 'output.txt'
    with open(output_file_path, 'a') as output_file:  # 'a' to append to the file
        output_file.write(output_content)

    print(header + table)

    for var in variables:
        pass

if __name__ == '__main__':
    main()
