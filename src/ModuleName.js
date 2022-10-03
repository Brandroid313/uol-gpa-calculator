import React, { useState } from 'react';
import { Box, Button, Layer, Text } from 'grommet';
import ModuleNameForm from './ModuleNameForm';

const ModuleName = () => {
    const [show, setShow] = React.useState();
    return (
      <Box>
        <Button label="show" onClick={() => setShow(true)} />
        {show && (
          <Layer
            onEsc={() => setShow(false)}
            onClickOutside={() => setShow(false)}
          >

            <ModuleNameForm/>
            <Button label="Cancel" onClick={() => setShow(false)} />
          </Layer>
        )}
      </Box>
    );
  }

  
export default ModuleName;