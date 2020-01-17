class Raith_library:
    def __init__(self,name,structures):
        '''name - name of GDSII library
        structures - array of Raith_structure objects in library
        structlist - ordered cell array of all names of structures found in
        library'''
        self.name = name
        self.snames = [s.name for s in structure]
        self.structures = structures
        self.structlist = self.snames

        ## Check for unique names
        if len(self.snames) != len(np.unique(self.snames)):
            raise RuntimeError("Raith_library:  all structures in library must have unique names.")

    def append(self, S):
        '''Raith_library.append(S) - append Raith_structure S (or array thereof) to library
        Argument:
        S - Raith_structure object to append to library'''
        if type(S)==list:
            for s in S:
                self.structures.append(s)
                self.snames.append(s.name)
        else:
            self.structures.append(S)
            self.snames.append(S.name)

    def writegds(self, output_dir=os.pwd(), dialect_choice='raith'):
        ''' function writegds(obj,varargin)
        Raith_library.writegds([outdir],[dialect]) - write Raith GDSII
        hierarchy file of all structures as [library.name].csf

        Arguments:
        outdir - string specifying directory in which to write .csf file
        [optional]; if called without arguments, file is written to working
        directory
        dialect - string specifying dialect of GDSII to write
        [optional]; may be 'Raith' (default) or 'plain'; if
        'plain' is selected, Raith curved elements are
        converted to boundary (polygon) or path elements, as
        appropriate
        See http://www.rulabinsky.com/cavd/text/chapc.html'''

        if dialect=='plain'
            ext = '.gds'
        elif dialect=='Raith'
            ext = '.csf'

        # Insert data checking here

def writerc(FileID,rectype,datatype,parameters):
    # Write GDSII record.
    #
    # Arguments:
    #   FileID - file identifier
    # 	rectype - 1-byte record type
    # 	datatype - 1-byte data type:
    #       00 - no data present
    #       01 - bit array (2 bytes)
    #       02 - 2-byte signed integer
    #       03 - 4-byte signed integer
    #       05 - 8-byte float
    #       06 - ASCII string
    # 	parameters - record parameters, of type defined by datatype
    #
    # The length of the record is computed, padded to an even
    # number of bytes if necessary, and the appropriate 2-byte
    # length header prepended before writing.

    pass
