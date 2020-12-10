import sys

zero  = ["   ***   ","  *   *  "," *     * "," *     * "," *     * ","  *   *  ","   ***   " ]
one   = ["     *   ","    **   ","   * *   ","     *   ","     *   ","     *   ","    ***  " ]
two   = [" ******* ","       * ","       * "," ******* "," *       "," *       "," ******* " ]
three = [" ******* ","       * ","       * "," ******* ","       * ","       * "," ******* " ]
four  = [" *     * "," *     * "," *     * "," ******* ","       * ","       * ","       * " ]
five  = [" ******* "," *       "," *       "," ******* ","       * ","       * "," ******* " ]
six   = [" ******* "," *       "," *       "," ******* "," *     * "," *     * "," ******* " ]
seven = [" ******* ","       * ","       * ","       * ","       * ","       * ","       * " ]
eight = [" ******* "," *     * "," *     * "," ******* "," *     * "," *     * "," ******* " ]
nine  = [" ******* "," *     * "," *     * "," ******* ","       * ","       * "," ******* " ]

#col = 9
#row = 7

Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

number = sys.argv[1]

row = 0

while row < 7:
   rowStr = ""
   for digit in number:
      rowStr += Digits[int(digit)][row]
   print(rowStr)
   row = row+1
