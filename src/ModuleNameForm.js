import React from 'react';
import { Box, Button, TextInput } from 'grommet';

const ModuleNameForm = () => {
    return (
      <Box>
        <div>Module name</div>
        <div>
            <TextInput
                placeholder="Enter Module Name"
            />
        </div>
        <div>
            Coursework 1 grade
            <TextInput
                placeholder="Enter Grade"
            />
            Coursework 2 grade
            <TextInput
                placeholder="Enter Grade"
            />
        </div>
        <div>
            <Button primary label="Submit" />
        </div>

      </Box>
    );
  }

  
export default ModuleNameForm;