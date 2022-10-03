import React, { useState } from 'react';
import {
  Accordion,
  AccordionPanel,
  Box,
  Button,
  Collapsible,
  Heading,
  Grommet,
  Layer,
  ResponsiveContext,
} from 'grommet';
import { FormClose, Notification } from 'grommet-icons';

import ModuleName from './ModuleName';

const theme = {
  global: {
    colors: {
      // brand: '#228BE6',
      brand: '#6f726e',
    },
    font: {
      family: 'Roboto',
      size: '18px',
      height: '20px',
    },
  },
};

const AppBar = (props) => (
  <Box
    tag='header'
    direction='row'
    align='center'
    justify='between'
    background='brand'
    pad={{ left: 'medium', right: 'small', vertical: 'small' }}
    elevation='medium'
    style={{ zIndex: '1' }}
    {...props}
  />
);


// class App extends Component {
  const App = () => {
    const [showSidebar, setShowSidebar] = useState(false);
    return (
      <Grommet theme={theme} full>
        <ResponsiveContext.Consumer>
        {size => (
          <Box fill>
            <AppBar>
              <Heading level='3' margin='none'>GPA Calculator</Heading>
              <Button
                icon={<Notification />}
                onClick={() => setShowSidebar(!showSidebar)}
              />
            </AppBar>
            <Box direction='row' flex overflow={{ horizontal: 'hidden' }}>
                <Box flex align='start' justify='start'>
                  GPA Calculator
                  <Accordion animate={true} multiple={true} margin='small'>

                    <AccordionPanel label='Level 4         %'>
                      <Accordion animate={true} multiple={true} margin='small'>
                        <AccordionPanel label='Module 1'>
                          <Box background='light-1'>Module 1 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 2'>
                          <Box height='small' width='xlarge' background='light-3'>
                              <div>Module 2........<Button primary color='#bd2519' label="Edit"/>........&#37;</div>
                              <ModuleName/>
                          </Box>
                          <Box height='small' background='light-1'>
                            <div>Coursework 1  &#37;</div>
                            <div>Coursework 2  &#37;</div>
                          </Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 3'>
                          <Box height='medium' background='light-1'>Module 3 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 4'>
                          <Box background='light-1'>Module 4 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 5'>
                          <Box background='light-1'>Module 5 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 6'>
                          <Box background='light-1'>Module 6 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 7'>
                          <Box background='light-1'>Module 7 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 8'>
                          <Box background='light-1'>Module 8 content</Box>
                        </AccordionPanel>
                      </Accordion>
                    </AccordionPanel>

                    <AccordionPanel label='Level 5         %'>
                      <Accordion animate={true} multiple={true} margin='small'>
                        <AccordionPanel label='Module 1'>
                          <Box background='light-1'>Module 1 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 2'>
                          <Box height='small' background='light-1'>Module 2 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 3'>
                          <Box height='medium' background='light-1'>Module 3 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 4'>
                          <Box background='light-1'>Module 4 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 5'>
                          <Box background='light-1'>Module 5 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 6'>
                          <Box background='light-1'>Module 6 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 7'>
                          <Box background='light-1'>Module 7 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 8'>
                          <Box background='light-1'>Module 8 content</Box>
                        </AccordionPanel>
                      </Accordion>
                    </AccordionPanel>

                    <AccordionPanel label='Level 6         %'>
                      <Accordion animate={true} multiple={true} margin='small'>
                        <AccordionPanel label='Module 1'>
                          <Box background='light-1'>Module 1 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 2'>
                          <Box height='small' background='light-1'>Module 2 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 3'>
                          <Box height='medium' background='light-1'>Module 3 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 4'>
                          <Box background='light-1'>Module 4 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 5'>
                          <Box background='light-1'>Module 5 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 6'>
                          <Box background='light-1'>Module 6 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 7'>
                          <Box background='light-1'>Module 7 content</Box>
                        </AccordionPanel>
                        <AccordionPanel label='Module 8'>
                          <Box background='light-1'>Module 8 content</Box>
                        </AccordionPanel>
                      </Accordion>
                    </AccordionPanel>

                  </Accordion>

                </Box>
                
                {(!showSidebar || size !== 'small') ? (
                <Collapsible direction="horizontal" open={showSidebar}>
                  <Box
                    width='medium'
                    background='light-2'
                    elevation='small'
                    align='center'
                    justify='center'
                  >
                    sidebar
                  </Box>
                  </Collapsible>
                ): (
                  <Layer>
                    <Box
                      background='light-2'
                      tag='header'
                      justify='end'
                      align='center'
                      direction='row'
                    >
                      <Button
                        icon={<FormClose />}
                        onClick={() => setShowSidebar(false)}
                      />
                    </Box>
                    <Box
                      fill
                      background='light-2'
                      align='center'
                      justify='center'
                    >
                      sidebar
                    </Box>
                  </Layer>
              )}
              </Box>
            </Box>
          )}
        </ResponsiveContext.Consumer>
      </Grommet>
    );
}

export default App;
