import React, { Component } from 'react';
import { DefaultTheme,Provider as PaperProvider, Drawer, Avatar, withTheme } from 'react-native-paper';
import { Button, Card, Title, Paragraph } from 'react-native-paper';
import { Platform, StyleSheet, Text, FlatList,View, ActivityIndicator,ScrollView, SafeAreaView } from 'react-native';

const theme = {
  ...DefaultTheme,
    roundness: 20,
    colors: {
      ...DefaultTheme.colors,
      primary: '#ff0000',
      accent: '#000000',
      text: "#cc1111",
      background: "#000000",
      contained: '#000000'
    },
    dark: true
  };

export default class App extends Component {
    
  render() {
    return (
            <PaperProvider theme={theme}>
    <ScrollView>
    <SafeAreaView>
      <View style={styles.container}>
        <Text style={styles.welcome}>C C  E v e n t s  A p p!</Text>
      </View>
            <Text></Text>
            <Card style = {styles.card}>
          <Card.Title title="Card Title" left={(props) => <Avatar.Icon {...props} icon="folder" />} />
          <Card.Content>
            <Title>Banana Cookoff!!</Title>
            <Paragraph>Its time to go Bananas!</Paragraph>
          </Card.Content>
          <Card.Cover source={{ uri: 'https://www.coloradocollege.edu/offices/communications/identity/img/email-header.png' }} />
          <Card.Actions>
            <Button>Cancel</Button>
            <Button>Ok</Button>
          </Card.Actions>
        </Card>
            <Text></Text>
        <Card style = {styles.card}>
          <Card.Title title="Card Title" subtitle="Card Subtitle" left={(props) => <Avatar.Icon {...props} icon="folder" />} />
          <Card.Content>
            <Title>Find Worner Campus Center</Title>
            <Paragraph>Where: Mathias @ 12PM, Bring blindfold</Paragraph>
          </Card.Content>
          <Card.Cover source={{ uri: 'https://www.coloradocollege.edu/offices/communications/identity/img/email-header.png' }} />
          <Card.Actions>
            <Button>Cancel</Button>
            <Button>Ok</Button>
          </Card.Actions>
        </Card>
            <Text></Text>
        <Card style = {styles.card}>
          <Card.Title title="Card Title" subtitle="Card Subtitle" left={(props) => <Avatar.Icon {...props} icon="folder" />} />
          <Card.Content>
            <Title>Card title</Title>
            <Paragraph>Card content</Paragraph>
          </Card.Content>
          <Card.Cover source={{ uri: 'https://www.coloradocollege.edu/offices/communications/identity/img/email-header.png' }} />
          <Card.Actions>
            <Button>Cancel</Button>
            <Button>Ok</Button>
          </Card.Actions>
        </Card>
    </SafeAreaView>
     </ScrollView>
    </PaperProvider>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop:20,
    //backgroundColor: '#F5FCFF',
  },
 card: {
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowRadius: 35,
 },
  welcome: {
     marginTop:15,
    fontSize: 22,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    marginBottom: 5,
  },
 loader: {
    flex:1,
     alignItems:'center',
     justifyContent:'center',
 }
});


