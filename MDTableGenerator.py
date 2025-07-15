class MDTableGenerator:
    def _mtg_make_table_line(self,fields):
        table_row = ["| "]
        for i in range(len(fields)):
            table_row.append(str(fields[i]))
            if i < len(fields) - 1:
                table_row.append(" | ")
        table_row.append(" |")
        return " ".join(table_row)
        
    def _mtg_make_table_header_sep(self, fields):
        header_separator = []
        for f in fields:
            header_separator.append(" -------- ")
        return header_separator
    
    def __init__(self, header:list):
        self.header = header
        self.rows = []
        self.header_seperator = self._mtg_make_table_header_sep(header)


    def add_row(self, row:list):
        if len(row) != len(self.header):
            raise IndexError("Row length does not match column header length")
        self.rows.append(row)

    def make_table_string(self) -> str:
        table_lines = [self._mtg_make_table_line(self.header),
                      self._mtg_make_table_line(self.header_seperator)]
        for t in self.rows:
            table_lines.append(self._mtg_make_table_line(t))
        
        table_str = ("\n").join(table_lines)
        return table_str
    
    def write_table_string(self, f):
        f.write(self.make_table_string())
