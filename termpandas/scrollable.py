import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import polars as pl
from blessings import Terminal
from curtsies import Input

#########################################################################
# Function to add a divider below the column names
def add_divider(input_str, length):
    # Split the message by the first new line character
    input_str = input_str.split('\n')
    # Add a divider of the same length as the terminal
    # After the first line of the message
    input_str.insert(1, '-'*length)
    # Join the message back together
    input_str = '\n'.join(input_str)
    return input_str

#########################################################################
# Function to process the logic of the DataFrame
def process_logic(t, df_input, start, end, start_row, end_row):
    diff = -999999
    if df_input.shape[1] > 1:
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
        # Calculate the length of the divider,
        # i.e., the length of the longest line in the message
        longest_line = 0
        message_lines = message.split('\n')
        for i in range(len(message_lines)):
            # strip the trailing white spaces
            temp = message_lines[i].rstrip()
            temp_len = len(temp)
            if temp_len > longest_line:
                longest_line = temp_len

        # Add the Divider
        message = add_divider(message, longest_line)

    elif df_input.shape[1] == 1:
        df = df_input.iloc[start_row:end_row, start:end+1]
        if t.width < 150:
            df = df.applymap(lambda x: str(x)[:26] + '...' if len(str(x)) > 30 else x)
        df_str = df.to_string()
        num_lines = df_str.count('\n')
        lines = df_str.split('\n')
        max_len = max([len(line) for line in lines])
        diff = max_len - t.width
        lines = [line.ljust(t.width) for line in lines]
        message = '\n'.join(lines)
        # Calculate the length of the divider,
        # i.e., the length of the longest line in the message
        longest_line = 0
        message_lines = message.split('\n')
        for i in range(len(message_lines)):
            # strip the trailing white spaces
            temp = message_lines[i].rstrip()
            temp_len = len(temp)
            if temp_len > longest_line:
                longest_line = temp_len
        message = add_divider(message, longest_line)

    return start, end, start_row, end_row, num_lines, message

#########################################################################
# Initial Printing Function
def initial_print(t, df_input, start, end, start_row, end_row, message, highlight, highlight_color, masks):
    # If masks is a pandas masks
    if masks is None:
        masks = {}
    # Foreground
    BRIGHT_WHITE = '\033[97m'

    # Background
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_GRAY = '\033[100m'

    # Reset
    RESET = '\033[0m'

    # Split Message by New Line
    message = message.split('\n')

    # Index_Color Maaping
    index_colors = {}

    # Key is either 'Red', 'Blue', 'Magenta', or 'Gray'
    # Value is a mask for a Pandas DataFrame
    for key, value in masks.items():
        # Filter the DataFrame by the mask
        df = df_input[value]
        # Get the indexes of the DataFrame
        indexes = df.index
        # Iterate over the indexes
        for index in indexes:
            # If the index is not in the mapping
            if index not in index_colors:
                # Add the index to the mapping
                index_colors[index] = key

    terminal_length = t.width
    # Print the DataFrame
    for i, line in enumerate(message):
        line = line.rstrip()
        line_length = len(line)
        num_spaces_to_add = terminal_length - line_length
        if i == 0 or i == 1:
            print(line + ' '*num_spaces_to_add)

        elif highlight != False:
            # if the index is for the first row being displayed
            if i == 2:
            # if i-2+start_row in index_colors:
                if highlight_color == 'Red':
                    print(BG_RED + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif highlight_color == 'Blue':
                    print(BG_BLUE + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif highlight_color == 'Magenta':
                    print(BG_MAGENTA + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif highlight_color == 'Gray':
                    print(BG_GRAY + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)

            elif i-2+start_row in index_colors and i != 2:
                if index_colors[i-2+start_row] == 'Red':
                    print(BG_RED + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Blue':
                    print(BG_BLUE + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Magenta':
                    print(BG_MAGENTA + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Gray':
                    print(BG_GRAY + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)

            else:
                print(line + ' '*num_spaces_to_add)

        else:
            if i-2+start_row in index_colors:
                if index_colors[i-2+start_row] == 'Red':
                    print(BG_RED + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Blue':
                    print(BG_BLUE + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Magenta':
                    print(BG_MAGENTA + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Gray':
                    print(BG_GRAY + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
            else:
                print(line + ' '*num_spaces_to_add)

    # Print total number of rows and columns
    if df_input.shape[1] > 1:
        info_str = f'Total Rows: {df_input.shape[0]}; Total Columns: {df_input.shape[1]}; Current Columns: {start+1}-{end+1}'
    if df_input.shape[1] == 1:
        info_str = f'Total Rows: {df_input.shape[0]}; Total Columns: {df_input.shape[1]}; Current Column: {start+1}'
    # Fill in the rest of the line with spaces
    info_str = info_str.ljust(t.width)
    print(info_str + t.clear_eol)

#########################################################################
# Printing After Input Logic
def after_print(t, df_input, start, end, start_row, end_row, num_lines, message, highlight, highlight_color, masks, row_counter):
    if masks is None:
        masks = {}
    moves = ''
    for i in range(num_lines):
        moves += t.move_up

    print(t.move_up + t.move_up + t.move_up + t.move_up + moves)
    # Foreground
    BRIGHT_WHITE = '\033[97m'

    # Background
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_GRAY = '\033[100m'

    # Reset
    RESET = '\033[0m'

    # Split Message by New Line
    message = message.split('\n')

    # Index_Color Maaping
    index_colors = {}

    # Key is either 'Red', 'Blue', 'Magenta', or 'Gray'
    # Value is a mask for a Pandas DataFrame
    for key, value in masks.items():
        # Filter the DataFrame by the mask
        df = df_input[value]
        # Get the indexes of the DataFrame
        indexes = df.index
        # Iterate over the indexes
        for index in indexes:
            # If the index is not in the mapping
            if index not in index_colors:
                # Add the index to the mapping
                index_colors[index] = key

    terminal_length = t.width
    # Print the DataFrame
    for i, line in enumerate(message):
        line = line.rstrip()
        line_length = len(line)
        num_spaces_to_add = terminal_length - line_length
        if i == 0 or i == 1:
            print(line + ' '*num_spaces_to_add)

        elif highlight != False:
            if i == row_counter:
                if highlight_color == 'Red':
                    print(BG_RED + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif highlight_color == 'Blue':
                    print(BG_BLUE + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif highlight_color == 'Magenta':
                    print(BG_MAGENTA + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif highlight_color == 'Gray':
                    print(BG_GRAY + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
            elif i-2+start_row in index_colors:
                if index_colors[i-2+start_row] == 'Red':
                    print(BG_RED + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Blue':
                    print(BG_BLUE + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Magenta':
                    print(BG_MAGENTA + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Gray':
                    print(BG_GRAY + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
            else:
                print(line + ' '*num_spaces_to_add)

        else:
            if i-2+start_row in index_colors:
                if index_colors[i-2+start_row] == 'Red':
                    print(BG_RED + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Blue':
                    print(BG_BLUE + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Magenta':
                    print(BG_MAGENTA + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
                elif index_colors[i-2+start_row] == 'Gray':
                    print(BG_GRAY + BRIGHT_WHITE + line + RESET + ' '*num_spaces_to_add)
            else:
                print(line + ' '*num_spaces_to_add)

    # Print total number of rows and columns
    if df_input.shape[1] > 1:
        info_str = f'Total Rows: {df_input.shape[0]}; Total Columns: {df_input.shape[1]}; Current Columns: {start+1}-{end+1}'
    if df_input.shape[1] == 1:
        info_str = f'Total Rows: {df_input.shape[0]}; Total Columns: {df_input.shape[1]}; Current Column: {start+1}'
    # Fill in the rest of the line with spaces
    info_str = info_str.ljust(t.width)
    print(info_str + t.clear_eol)

#########################################################################
# Function to print the DataFrame
def tprint(df_input,
           num_rows=10,
           highlight=True,
           highlight_color='Gray',
           return_row=False,
           masks=None):
    row_counter = 2
#########################################################################
# Ensure df_input is a Pandas DataFrame
    # if df_input is a pandas Series
    # convert it to a DataFrame
    if isinstance(df_input, pd.Series):
        df_input = pd.DataFrame(df_input)

    # if df_input is a polars DataFrame
    # convert it to a pandas DataFrame
    if isinstance(df_input, pl.DataFrame):
        df_input = df_input.to_pandas()

    # if df_input is a polars Series
    # convert it to a pandas Series
    if isinstance(df_input, pl.Series):
        df_input = df_input.to_pandas()
        # Convert the pandas Series to a DataFrame
        df_input = pd.DataFrame(df_input)

    # Initialize the terminal
    t = Terminal()
    # Set the starting row to 0
    start_row = 0
    # Set the ending row to the input number of rows
    end_row = num_rows

#########################################################################
# Initial Generation of the DataFrame
    with Input(keynames='curses') as input_generator:
        start = 0
        end = 0
        start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row) 
        initial_print(t, df_input, start, end, start_row, end_row, message, highlight, highlight_color, masks)

#########################################################################
# Input Logic
        for e in input_generator:
#########################################################################
# Press 'q' to quit
            if e in ['q']:  # quit
                break
#########################################################################
# Press '\n' to select a row
            if e in ['\n']:  # select row
                # add conditions to return only the highlighted row
                if highlight and return_row == True:
                    # Calculate the highlighted row
                    return df_input.iloc[[start_row + row_counter - 2]]
#########################################################################
# Press 'h' or 'KEY_LEFT' to move left
            elif e in ['h', 'KEY_LEFT'] and start > 0:  # move left;
                start -= 1
                end = start + 1
                start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row) 

#########################################################################
# Press 'l' or 'KEY_RIGHT' to move right
            elif e in ['l', 'KEY_RIGHT'] and df_input.shape[1] > 1:  # move right;
                # if the `end` is not the last column then only move to right
                if end != len(df_input.columns) - 1:      
                    start += 1
                    end = start + 1
                    start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row) 


#########################################################################
# Press 'k' or 'KEY_UP' to move up
            elif e in ['k', 'KEY_UP']:  # move up; 
                if highlight == True:
                    if row_counter > 2:
                        row_counter -= 1
                    if row_counter == 2 and start_row > 0:
                        start_row -= 1 
                        end_row -= 1 
                        end = start + 1
                        start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row) 
                else:
                    if start_row > 0:
                        start_row -= 1 
                        end_row -= 1 
                        end = start + 1
                        start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row)

#########################################################################
# Press 'j' or 'KEY_DOWN' to move down
            elif e in ['j', 'KEY_DOWN']:  # move down;
                if highlight == True:
                    if row_counter < num_lines+1:
                        row_counter += 1
                    if row_counter == num_lines+1 and end_row < len(df_input):
                        start_row += 1
                        end_row += 1
                        end = start + 1
                        start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row) 
                else:
                    if end_row < len(df_input):
                        start_row += 1
                        end_row += 1
                        end = start + 1
                        start, end, start_row, end_row, num_lines, message = process_logic(t, df_input, start, end, start_row, end_row)

#########################################################################
# Print DataFrame after input logic
            after_print(t, df_input, start, end, start_row, end_row, num_lines, message, highlight, highlight_color, masks, row_counter)

# Example Usage
# tprint(df, num_rows=10)
