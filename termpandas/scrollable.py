import warnings
warnings.filterwarnings("ignore")

import pandas as pd
from blessings import Terminal
from curtsies import Input

def tprint(df_input, num_rows=10):
    t = Terminal()
    start = 0
    end = 0
    start_row = 0
    end_row = num_rows

    diff = -999999

    with Input(keynames='curses') as input_generator:
        # Print Number of columns
        while diff < 0 and end < len(df_input.columns):
            df = df_input.iloc[start_row:end_row, start:end+1]
            if t.width < 150:
                df = df.applymap(lambda x: str(x)[:26] + '...' if len(str(x)) > 30 else x)
            df_str = df.to_string()
            num_lines = df_str.count('\n')
            lines = df_str.split('\n')
            max_len = max([len(line) for line in lines])
            diff = max_len - t.width
            lines = [line.ljust(t.width) for line in lines]
            if diff < 0 and end < len(df_input.columns):
                message = '\n'.join(lines)
                end += 1
        end -= 1

        print(message + t.clear_eol)
        print()
        # Print total number of rows and columns
        info_str = f'Total Rows: {df_input.shape[0]}; Total Columns: {df_input.shape[1]}; Current Columns: {start+1}-{end+1}'
        # Fill in the rest of the line with spaces
        info_str = info_str.ljust(t.width)
        print(t.move_up + info_str + t.clear_eol)

        for e in input_generator:
            if e in ['q']:  # quit
                break
            elif e in ['h', 'KEY_LEFT'] and start > 0:  # move left;
                start -= 1
                end = start + 1
                diff = -999999
                while diff < 0 and end < len(df_input.columns):
                    df = df_input.iloc[start_row:end_row, start:end+1]
                    if t.width < 150:
                        df = df.applymap(lambda x: str(x)[:26] + '...' if len(str(x)) > 30 else x)
                    df_str = df.to_string()
                    num_lines = df_str.count('\n')
                    lines = df_str.split('\n')
                    max_len = max([len(line) for line in lines])
                    diff = max_len - t.width
                    lines = [line.ljust(t.width) for line in lines]
                    if diff < 0 and end < len(df_input.columns):
                        message = '\n'.join(lines)
                        end += 1
                end -= 1

            elif e in ['l', 'KEY_RIGHT']: # move right;
                # if the `end` is not the last column then only move to right
                if end != len(df_input.columns) - 1:      
                    start += 1
                    end = start + 1
                    diff = -999999
                    while diff < 0 and end < len(df_input.columns):
                        df = df_input.iloc[start_row:end_row, start:end+1]
                        if t.width < 150:
                            df = df.applymap(lambda x: str(x)[:26] + '...' if len(str(x)) > 30 else x)
                        df_str = df.to_string()
                        num_lines = df_str.count('\n')
                        lines = df_str.split('\n')
                        max_len = max([len(line) for line in lines])
                        diff = max_len - t.width
                        lines = [line.ljust(t.width) for line in lines]
                        if diff < 0 and end < len(df_input.columns):
                            message = '\n'.join(lines)
                            end += 1
                    end -= 1


            elif e in ['k', 'KEY_UP'] and start_row > 0:  # move up; 
                start_row -= 1 
                end_row -= 1 
                end = start + 1
                diff = -999999
                while diff < 0 and end < len(df_input.columns):
                    df = df_input.iloc[start_row:end_row, start:end+1]
                    if t.width < 150:
                        df = df.applymap(lambda x: str(x)[:26] + '...' if len(str(x)) > 30 else x)
                    df_str = df.to_string()
                    num_lines = df_str.count('\n')
                    lines = df_str.split('\n')
                    max_len = max([len(line) for line in lines])
                    diff = max_len - t.width
                    lines = [line.ljust(t.width) for line in lines]
                    if diff < 0 and end < len(df_input.columns):
                        message = '\n'.join(lines)
                        end += 1
                end -= 1

            elif e in ['j', 'KEY_DOWN'] and end_row < len(df_input):  # move down;
                start_row += 1
                end_row += 1
                end = start + 1
                diff = -999999
                while diff < 0 and end < len(df_input.columns):
                    df = df_input.iloc[start_row:end_row, start:end+1]
                    if t.width < 150:
                        df = df.applymap(lambda x: str(x)[:26] + '...' if len(str(x)) > 30 else x)
                    df_str = df.to_string()
                    num_lines = df_str.count('\n')
                    lines = df_str.split('\n')
                    max_len = max([len(line) for line in lines])
                    diff = max_len - t.width
                    lines = [line.ljust(t.width) for line in lines]
                    if diff < 0 and end < len(df_input.columns):
                        message = '\n'.join(lines)
                        end += 1
                end -= 1

            moves = ''
            for i in range(num_lines):
                moves += t.move_up

            print(t.move_up + t.move_up + moves + message + t.clear_eol)
            print()
            # Print total number of rows and columns
            info_str = f'Total Rows: {df_input.shape[0]}; Total Columns: {df_input.shape[1]}; Current Columns: {start+1}-{end+1}'
            # Fill in the rest of the line with spaces
            info_str = info_str.ljust(t.width)
            print(t.move_up + info_str + t.clear_eol)

# Example Usage
# tprint(df, num_rows=10)
