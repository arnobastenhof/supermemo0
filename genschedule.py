import argparse
import sys

from calendar import monthrange, month_name

def parse_args():
  # Parse command line arguments
  parser = argparse.ArgumentParser(description = 'Schedule generator.')
  parser.add_argument('year', metavar = 'Y', type = int, nargs = '?',
    default = 2018, help = 'The year at which to start. Default 2018.')
  parser.add_argument('month', metavar = 'M', type = int, nargs = '?',
    default = 1, help = 'The month at which to start (1-12). Default 1.')
  parser.add_argument('span', metavar = 'S', type = int, nargs = '?',
    default = 12, help = 'Number of months. Default 12.')
  args = parser.parse_args()

  # Validate arguments
  if args.year < 0:
    sys.exit('Invalid year. Must be >= 0.')
  if args.month < 1 or args.month > 12:
    sys.exit('Invalid month. Must be >=1 and <= 12.')
  if args.span < 1:
    sys.exit('Invalid span. Must be >= 1.')

  return args

def main():
  # Parse command line arguments
  args = parse_args()

  with open('tex/calendar.tex', 'w') as out:

    for i in range(0, args.span):

      # Output table header
      out.write('\\begin{center}\n\\begin{tabular}{|\\C{0.05}|\\C{0.8}|}\\hline\n')
      out.write('\\multicolumn{2}{|c|}{\\T\\B ')

      # Output month
      month = (args.month + i) % 12
      month = month if month != 0 else 12
      out.write(month_name[month])
      out.write(' ')

      # Output year
      year = args.year + ((args.month + i - 1) // 12)
      out.write(str(year))
      out.write('}\\\\ \\hline\n')

      # Output one row per day
      days = monthrange(year, month)[1]
      for d in range(1, days + 1):
        out.write('\\T\\B ')
        out.write(str(d))
        out.write(' & \\\\ \\hline\n')

      # Output table footer
      out.write('\\end{tabular}\n\\end{center}\\clearpage\n\n')

if __name__ == '__main__':
  main()
